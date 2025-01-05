import streamlit as st

def run():
    st.title(
        ':blue[ДЗ1. Анализ температурных данных и мониторинг текущей температуры через OpenWeatherMap API] :sunglasses:')

    st.header('Описание задания:')
    st.write(
        '''
        Вы аналитик в компании, занимающейся изучением климатических изменений и мониторингом температур в разных городах. 
        Вам нужно провести анализ исторических данных о температуре для выявления сезонных закономерностей и аномалий. 
        Также необходимо подключить API OpenWeatherMap для получения текущей температуры в выбранных городах и сравнить
        её с историческими данными.
        '''
    )
    st.header('Цели задания:')
    st.write(
        '''
        1. Провести анализ временных рядов, включая:\n
        \t* Вычисление скользящего среднего и стандартного отклонения для сглаживания температурных колебаний.\n
        \t* Определение аномалий на основе отклонений температуры от  скользящее среднее ±2σ.\n
        \t* Построение долгосрочных трендов изменения температуры.\n
        \t* Любые дополнительные исследования будут вам в плюс.\n
        2. Осуществить мониторинг текущей температуры:\n
        \t* Получить текущую температуру через OpenWeatherMap API.\n
        \t* Сравнить её с историческим нормальным диапазоном для текущего сезона.\n
        3. Разработать интерактивное приложение:\n
        \t* Дать пользователю возможность выбрать город.\n
        \t* Отобразить результаты анализа температур, включая временные ряды, сезонные профили и аномалии.\n
        \t* Провести анализ текущей температуры в контексте исторических данных.\n
        '''
    )
    st.header('Описание данных')
    st.write(
        '''
        Исторические данные о температуре содержатся в файле temperature_data.csv, включают:\n
        \t"city": Название города.\n
        \t"timestamp": Дата (с шагом в 1 день).\n
        \t"temperature": Среднесуточная температура (в °C).\n
        \t"season": Сезон года (зима, весна, лето, осень).\n
        '''
    )
