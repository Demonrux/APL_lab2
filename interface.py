import logic


def command_interface():

    commands = {
        '1': {
            'name': '2-D график зависимости средней загрузки от длины',
            'func': logic.plot_mean_dwt_vs_length
        },
        '2': {
            'name': 'Распределение кораблей по типам',
            'func': logic.plot_ship_types_pie
        },
        '3': {
            'name': 'Гистограмма по годам постройки',
            'func': logic.plot_ships_by_built_year
        },
        '4': {
            'name': '2D гистограмма: годы постройки vs грузоподъемность',
            'func': logic.plot_2d_histogram
        },
        '5': {
            'name': 'Парная диаграмма для ирисов',
            'func': logic.plot_iris_pairplot_detailed
        },
        '6': {
            'name': 'Скрипичные диаграммы для ирисов',
            'func': logic.plot_iris_violin_single
        },
        '7': {
            'name': 'Выход',
            'func': None
        }
    }

    while True:

        for key, value in commands.items():
            print(f"{key}. {value['name']}")

        choice = input("Выберите действие (1-7): ").strip()

        if choice == '7':
            print("Выход...")
            break

        if choice in commands:
            try:
                commands[choice]['func']()
            except Exception as error:
                print(f" Ошибка при выполнении: {error}")
        else:
            print(" Неизвестная команда.")
