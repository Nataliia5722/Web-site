from selenium import webdriver
import pytest

browser = webdriver.Chrome('C:\\Users\\Kryvo\\OneDrive\\Documents\\chromedriver.exe')

#Test001 Проверка отображения страницы (OE-2)
def test_opening_page():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")

#TC-002  Проверка выбора размерности матрицы (FR-1)
def test_rows_colomns():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")
    browser.find_element_by_id('add').click()
    browser.find_element_by_id('rowV1').send_keys('0')
    browser.find_element_by_id('rowV2').send_keys('0')
    browser.find_element_by_id('colV1').send_keys('0')
    browser.find_element_by_id('colV2').send_keys('0')
    #assert browser.find_element_by_id('submitButton').click()==None
    browser.switch_to.alert


#TC-003 Проверка выбора размерности матрицы (FR-1)
def test_rows_colomns_2():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")
    browser.find_element_by_id('add').click()
    browser.find_element_by_id('rowV1').send_keys('3')
    browser.find_element_by_id('rowV2').send_keys('3')
    browser.find_element_by_id('colV1').send_keys('4')
    browser.find_element_by_id('colV2').send_keys('4')
    assert browser.find_element_by_id('submitButton').click()==None


#TC-005 Обновление результата операции при нажатии кнопки (FR-2)
def test_show_result():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")
    browser.find_element_by_id('transpose').click()
    browser.find_element_by_id('rowV').send_keys('2')
    browser.find_element_by_id('colV').send_keys('1')
    browser.find_element_by_id('submitButton').click()
    browser.find_element_by_id('cell_0_0').send_keys('2')
    browser.find_element_by_id('cell_1_0').send_keys('3')
    browser.find_element_by_id('calc').click()
    browser.find_element_by_id('calc').click()
    assert len(browser.find_elements_by_class_name('solutionTable')) == 1

#TC-006 Вывод сообщения об ошибке при некорректном вводе данных (FR-3)
def test_number_of_elements_for_determinant():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")
    browser.find_element_by_id('determinant').click()
    browser.find_element_by_id('rowV').send_keys('2')
    browser.find_element_by_id('colV').send_keys('3')
    browser.find_element_by_id('submitButton').click()
    browser.switch_to.alert


#TC-007 Проверка корректности ввода размерности матрицы для подсчета детерминанта (FR-3)
def test_number_of_elements_for_determinant():
    print("Test1")
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\index.html")
    browser.find_element_by_id('determinant').click()
    browser.find_element_by_id('rowV').send_keys('4')
    browser.find_element_by_id('colV').send_keys('4')
    browser.find_element_by_id('submitButton').click()
    assert len(browser.find_elements_by_id('cell_0_0'))!=0




#TC-004 Ввод элементов матрицы (FR-2)
def test_entering_elements():
    browser.get("C:\\Users\\Kryvo\\OneDrive\\Рабочий стол\\MatrixCalculator\\templates\\determinant.html")
    browser.find_element_by_id('rowV').send_keys('3')
    browser.find_element_by_id('colV').send_keys('3')
    browser.find_element_by_id('submitButton').click()
    browser.find_element_by_id('cell_0_0').send_keys('2')
    browser.find_element_by_id('cell_0_1').send_keys('3')
    browser.find_element_by_id('cell_0_2').send_keys('3')
    browser.find_element_by_id('cell_1_0').send_keys('3')
    browser.find_element_by_id('cell_1_1').send_keys('4')
    browser.find_element_by_id('cell_1_2').send_keys('7')
    browser.find_element_by_id('cell_2_0').send_keys('2')
    browser.find_element_by_id('cell_2_1').send_keys('5')
    browser.find_element_by_id('cell_2_2').send_keys('7')
    browser.find_element_by_id('calc').click()
    browser.find_element_by_class_name('formText').text == -14
