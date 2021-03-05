FROM joyzoursky/python-chromedriver:3.8-selenium

ADD hub_test_basic.py /

CMD [ "python", "./hub_test_basic.py" ]