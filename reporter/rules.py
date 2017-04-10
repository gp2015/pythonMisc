from sys import argv
import json


def get_lender_data(lender_data = argv[1]):
    lender_data = open(lender_data, 'r')
    lender_data = lender_data.read()
    lender_data_json = json.loads(lender_data)
    return lender_data_json


def get_consumer_data(consumer_data = argv[2]):
    consumer_data = open(consumer_data, 'r')
    consumer_data = consumer_data.read()
    consumer_data_json = json.loads(consumer_data)
    return consumer_data_json


def generate_report_data(lender_data, consumer_data, rule):
    rule_name = str(rule)
    rule = rules(rule, lender_data, consumer_data)

    report_data = {
        "first_name": lender_data['first_name'],
        "last_name": lender_data['last_name'],
        "bank_account_balance": consumer_data['bank_account_balance'], 
        rule_name: rule
    }

    report_data_json = json.dumps(report_data)
    return report_data_json


def rules(rule, lender_data, consumer_data):
    if (rule == "monthly_income"):
        monthly_income = (lender_data['salary'] / 12)
        monthly_income = round(monthly_income, 2)
        return monthly_income

    if (rule == "bi_weekly_income"):
        bi_weekly_income = (lender_data['salary'] / 26)
        bi_weekly_income = round(bi_weekly_income, 2)
        return bi_weekly_income


def generate_report(report_data):
    print(report_data)


def tests():
    get_consumer_data()
    get_lender_data()


def template1():
    lender_data = get_lender_data()
    consumer_data = get_consumer_data()
    report_data = generate_report_data(lender_data, consumer_data, "monthly_income")
    generate_report(report_data)


def template2():
    lender_data = get_lender_data()
    consumer_data = get_consumer_data()
    report_data = generate_report_data(lender_data, consumer_data, "bi_weekly_income")
    generate_report(report_data)



tests()
template1()
template2()
