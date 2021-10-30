python %cd%\util\generate_page.py home welcome --main --next /Java-Data-Pack-Tutorial/pages/introduction/your_first_data_pack.html

python %cd%\util\generate_page.py introduction your_first_data_pack --next /Java-Data-Pack-Tutorial/pages/introduction/your_first_function.html
python %cd%\util\generate_page.py introduction your_first_function --next /Java-Data-Pack-Tutorial/pages/introduction/ticks.html
python %cd%\util\generate_page.py introduction ticks --prev /Java-Data-Pack-Tutorial/pages/introduction/ticks.html --next /Java-Data-Pack-Tutorial/pages/introduction/functions_with_delays.html