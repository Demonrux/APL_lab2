import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

df_ships = pd.read_csv('files/Cleaned_ships_data.csv')
df_iris = pd.read_csv('files/IRIS.csv')
df_science_salary = pd.read_csv('files/Data_Science_Salary_2021_to_2023.csv')


def plot_mean_dwt_vs_length():

    length_bins = np.linspace(df_ships['length'].min(), df_ships['length'].max(), 20)

    df_ships['length_bin'] = pd.cut(df_ships['length'], bins=length_bins)

    df_binned = df_ships.groupby('length_bin').agg(
        mean_length=('length', 'mean'),
        mean_dwt=('dwt', 'mean'),
        count=('dwt', 'count')
    ).reset_index()

    df_binned_filtered = df_binned[df_binned['count'] >= 3]

    plt.figure(figsize=(12, 6))
    plt.plot(df_binned_filtered['mean_length'], df_binned_filtered['mean_dwt'], 's-', linewidth=2, markersize=6)
    plt.xlabel('Длина корабля')
    plt.ylabel('Средняя максимальная загрузка ')
    plt.title('Зависимость средней грузоподъемности от длины корабля')
    plt.grid(True)
    plt.show()


def plot_ship_types_pie():

    ship_type_counts = df_ships['ship_name'].value_counts()

    threshold = 5
    mask = ship_type_counts < threshold

    main_categories = ship_type_counts[~mask]
    other_categories = ship_type_counts[mask]

    plot_data = main_categories.copy()
    plot_data['Другие'] = other_categories.sum()

    plt.figure(figsize=(10, 6))
    plt.pie(plot_data.values, labels=plot_data.index, autopct='%1.1f%%')
    plt.title('Распределение кораблей по типам')
    plt.axis('equal')
    plt.show()


def plot_ships_by_built_year():

    plt.figure(figsize=(12, 6))
    plt.hist(df_ships['built_year'], bins=30, alpha=0.7, edgecolor='black')
    plt.xlabel('Год постройки')
    plt.ylabel('Количество кораблей')
    plt.title('Распределение количества кораблей по годам постройки')
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_2d_histogram():

    dwt_bins = np.linspace(df_ships['dwt'].min(), df_ships['dwt'].max(), 21)

    plt.figure(figsize=(12, 6))
    h = plt.hist2d(df_ships['built_year'], df_ships['dwt'],
                   bins=[30, dwt_bins],
                   cmap='viridis')

    plt.colorbar(h[3], label='Количество кораблей')
    plt.xlabel('Год постройки')
    plt.ylabel('Максимальная загрузка')
    plt.title('Распределение кораблей по году постройки и грузоподъемности')
    plt.show()


def plot_iris_pairplot():

    seaborn.pairplot(df_iris)
    plt.suptitle('Парная диаграмма для датасета Iris')
    plt.show()


def plot_iris_violin():

    df_melted = df_iris.melt(id_vars='species',
                        value_vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                        var_name='characteristic',
                        value_name='value')

    plt.figure(figsize=(10, 6))
    seaborn.violinplot(data=df_melted, x='characteristic', y='value',
                   hue='species', palette='pastel', split=True)
    plt.title('Скрипичные диаграммы всех характеристик ирисов')
    plt.xlabel('Характеристика')
    plt.ylabel('Значение (см)')
    plt.legend(title='Вид ириса')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_salary_by_experience():
    plt.figure(figsize=(12, 6))

    seaborn.violinplot(data=df_science_salary, x='experience_level', y='salary_in_usd')

    plt.title('Плотность распределения зарплат')
    plt.xlabel('Уровень опыта')
    plt.ylabel('Зарплата в USD')
    plt.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_paying_jobs():

    top_jobs = df_science_salary.groupby('job_title')['salary_in_usd'].median().nlargest(10)

    plt.figure(figsize=(12, 6))
    bars = plt.barh(top_jobs.index, top_jobs.values)

    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2,
                 f'${width:,.0f}', ha='left', va='center')

    plt.xlabel('Медианная зарплата (USD)')
    plt.title('Топ-10 самых высокооплачиваемых IT-должностей')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_salary_trends_by_year():

    plt.figure(figsize=(12, 6))

    seaborn.lineplot(data=df_science_salary, x='work_year', y='salary_in_usd',
                 hue='experience_level', estimator='median',)

    plt.title('Динамика медианных зарплат по годам и уровням опыта')
    plt.xlabel('Год')
    plt.ylabel('Зарплата в USD')
    plt.legend(title='Уровень опыта')
    plt.grid(True, alpha=0.3)
    plt.show()



