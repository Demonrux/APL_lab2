import logic as lg


def console_interface():

    commands = {
        '1': {
            'name': '2-D график зависимости средней загрузки от длины',
            'func': lg.plot_mean_dwt_vs_length
        },
        '2': {
            'name': 'Распределение кораблей по типам',
            'func': lg.plot_ship_types_pie
        },
        '3': {
            'name': 'Гистограмма по годам постройки',
            'func': lg.plot_ships_by_built_year
        },
        '4': {
            'name': '2D гистограмма: годы постройки vs грузоподъемность',
            'func': lg.plot_2d_histogram
        },
        '5': {
            'name': 'Парная диаграмма для ирисов',
            'func': lg.plot_iris_pairplot
        },
        '6': {
            'name': 'Скрипичные диаграммы для ирисов',
            'func': lg.plot_iris_violin
        },
        '7': {
            'name': 'Распределение зарплат по уровням опыта (Experience Level)',
            'func': lg.plot_salary_by_experience
        },
        '8': {
            'name': 'Топ-10 самых высокооплачиваемых должностей',
            'func': lg.plot_top_paying_jobs

        },
        '9': {
            'name': 'Динамика зарплат по годам',
            'func': lg.plot_salary_trends_by_year
        },
        '10': {
            'name': 'Выход',
            'func': None
        }
    }

    while True:

        print("Задание 1(IRIS.csv, Cleaned_ships.csv):\n" + "_"*10)
        for key, value in commands.items():
            print(f"{key}. {value['name']}")
            if key == "6":
                print("_"*10 + "\nЗадание 2(Data_Science_Salary_2021_to_2023.csv):\n" + "_"*10)
            if key == "9":
                print("_"*10)

        choice = input("Выберите действие (1-7): ").strip()

        if choice == '10':
            print("Выход...")
            break

        if choice in commands:
            try:
                commands[choice]['func']()
            except Exception as error:
                print(f" Ошибка при выполнении: {error}")
        else:
            print(" Неизвестная команда.")
