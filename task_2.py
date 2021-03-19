# from selenium import webdriver
# Задачу выполнил в два подхода, потому сделал через два менеджера контекста, но можно обойтись и без файлов, а сразу
# в скрипте совевршить все манипуляции.

if __name__ == '__main__':
    # Закоментировал получение данных с Wiki
    # opts = webdriver.ChromeOptions()
    # browser = webdriver.Chrome(options=opts, executable_path=r'C:\Users\Василий\Downloads\chromedriver.exe')
    # browser.implicitly_wait(10)  # секунд
    # browser.get(
    #     r'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')
    # with open('animals.txt', 'w', encoding='UTF-8') as f:
    #     # Взял с запасом, вручную удалил английские слова
    #     for _ in range(99):
    #         html_text = browser.find_element_by_class_name(name='mw-category-group').text
    #         f.write(html_text)
    #         f.write('\n')
    #         search_button = browser.find_element_by_link_text('Следующая страница')
    #         search_button.click()

    with open('animals.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        list_animals = text.split('\n')
        res_dict = {}
        char = None
        for el in list_animals:
            # Выполнил небольшую очистку данных, исключив животных с уточнениями в скобках, (род), (семейство), прочее
            if el.find('('):

                if len(el) == 1 and char != el:
                    res_dict[el] = 0
                    char = el
                else:
                    res_dict[char] += 1
    total = 0
    for key, value in res_dict.items():
        print(f'{key}: {value}')
        total += value
    print(f'Всего: {total}')

# Результат
# А: 1094
# Б: 1399
# В: 484
# Г: 823
# Д: 527
# Е: 27
# Ж: 209
# З: 392
# И: 317
# К: 2006
# Л: 665
# М: 1050
# Н: 278
# О: 609
# П: 1458
# Р: 379
# С: 1648
# Т: 757
# У: 181
# Ф: 152
# Х: 206
# Ц: 11
# Ч: 440
# Ш: 97
# Щ: 38
# Э: 33
# Я: 152
# Всего: 15432
