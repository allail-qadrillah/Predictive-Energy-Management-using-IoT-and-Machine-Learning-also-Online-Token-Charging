import onnxruntime
from .holiday.get_holiday import Get_Holiday
from .weather.get_weather import Get_Weather
import pandas as pd
import numpy as np

class API():
    def __init__(self):
        self.model = "./model/modelv1.h5"
        self.get_holiday_instance = Get_Holiday()
        self.get_weather_instance = Get_Weather()

    def get_holiday_range(self, day: int) -> list[int]:
        "mendapatkan range hari libur dengan nilai 0 dan 1 tanggal dari hari ini sampai (day) hari"
        return self.get_holiday_instance.get_holiday_range(day)

    def get_weather_range(self, day: int) -> list[int]:
        "mendapatkan range cuaca"
        return self.get_weather_instance.get_weather_range(day)

    def get_value_conditions(self, conditions):
        if conditions == "Clear":
            return [1, 0, 0, 0, 0]
        elif conditions == "Overcast":
            return [0, 1, 0, 0, 0]
        elif conditions == "Partially cloudy":
            return [0, 0, 1, 0, 0]
        elif conditions == "Rain, Overcast":
            return [0, 0, 0, 1, 0]
        elif conditions == "Rain, Partially cloudy":
            return [0, 0, 0, 0, 1]

    def get_input(self, count: int):
        """
        Return dataframe input dengan kolom yang berisi cuaca, libur, dan kondisi cuaca. Nilai libur dari hari ini sampai (count)
        count : range input (untuk berapa hari?)
        """
        holidays = self.get_holiday_range(count)
        weathers = self.get_weather_range(count)

        df = pd.DataFrame(columns=['temp', 'feelslike', 'libur', 'conditions_Clear',
                                   'conditions_Overcast', 'conditions_Partially cloudy',
                                   'conditions_Rain, Overcast', 'conditions_Rain, Partially cloudy'])
        data_input = []
        for holiday, weather in zip(holidays, weathers):
            data_input.append({
                'temp': weather['temp'],
                'feelslike': weather['feelslike'],
                'libur': float(holiday),
                'conditions_Clear': float(self.get_value_conditions(weather['conditions'])[0]),
                'conditions_Overcast': float(self.get_value_conditions(weather['conditions'])[1]),
                'conditions_Partially cloudy': float(self.get_value_conditions(weather['conditions'])[2]),
                'conditions_Rain, Overcast': float(self.get_value_conditions(weather['conditions'])[3]),
                'conditions_Rain, Partially cloudy': float(self.get_value_conditions(weather['conditions'])[4])
            })

        return pd.concat([df, pd.DataFrame(data_input)], ignore_index=True)

    def get_prediction(self, day: int) -> list:
        """
        mendapatkan prediksi dari model dengan input hari
        """

        session = onnxruntime.InferenceSession('./model/modelv1.onnx')

        # Prepare the input data
        input_data = np.array(self.get_input(day))

        input_data = input_data.reshape(
            (len(input_data), 8, 1)).astype(np.float32)

        # Run the model to get predictions
        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name
        return session.run([output_name], {input_name: input_data})[0].tolist()

api = API()

weather = api.get_weather_range()

print(weather)