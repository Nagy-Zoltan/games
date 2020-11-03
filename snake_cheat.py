from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('file:///C:/Users/Lenovo/Desktop/Chrome/snake.html')
body = browser.find_elements_by_xpath('//body')[0]

def left():
    body.send_keys(Keys.ARROW_LEFT)
def right():
    body.send_keys(Keys.ARROW_RIGHT)
def up():
    body.send_keys(Keys.ARROW_UP)
def down():
    body.send_keys(Keys.ARROW_DOWN)
    
browser.execute_script('get_fx = () => food_x')
browser.execute_script('get_fy = () => food_y')
browser.execute_script('get_snake = () => snake.body')
browser.execute_script('get_direction = () => snake.direction')

while True:
    food_x = browser.execute_script('return get_fx()')
    food_y = browser.execute_script('return get_fy()')
    if 40 <= food_x <= 550 and 40 <= food_y <= 550:
        while True:
            food_x = browser.execute_script('return get_fx()')
            food_y = browser.execute_script('return get_fy()')
            snake = browser.execute_script('return get_snake()')
            direction = browser.execute_script('return get_direction()')
            if snake[-1][1] <= 40 and direction == 'up':
                if 0 <= snake[-1][0] <= 300:
                    right()
                else:
                    left()
            elif snake[-1][1] >= 550 and direction == 'down':
                if 0 <= snake[-1][0] <= 300:
                    right()
                else:
                    left()
            elif snake[-1][0] == 40 and direction == 'left':
                if 0 <= snake[-1][1] <= 300:
                    down()
                else:
                    up()
            elif snake[-1][0] == 550 and direction == 'right':
                if 0 <= snake[-1][1] <= 300:
                    down()
                else:
                    up()
            if food_x < 40 or food_y < 40 or food_x > 550 or food_y > 550:
                break
    else:
        continue