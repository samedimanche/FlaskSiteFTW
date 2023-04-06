from flask import Flask, render_template, request, url_for
from course import get_course
from lbjup import get_recommendation
from tours import get_recommendation_tours

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("home.html")

@app.route('/course', methods=['GET', 'POST'])
def course():
    get_course_currency = get_course()
    return render_template('course.html', thb_rub=get_course_currency[0], usd_rub=get_course_currency[1], eur_rub = get_course_currency[2],
                           try_rub = get_course_currency[3], egp_rub = get_course_currency[4], aed_rub = get_course_currency[5],
                           vef_rub = get_course_currency[6], cup_rub = get_course_currency[7], vnd_rub = get_course_currency[8])


@app.route('/where_to_go', methods=['GET', 'POST'])
def where_to_go():
    if request.method == 'POST':
        try:
            # get user inputs from dropdown menus
            sum_for_vocation = float(request.form['sum_for_vocation'])
            city_preference = request.form['city_preference']
            age = int(request.form['age'])
            vacation_preference = request.form['vacation_preference']
            transport_preference = request.form['transport_preference']
            family_members = (request.form['family_members'])
            # use neural network to get recommendation
            if sum_for_vocation and age:
                text_fror_recommendation = 'Вам следует выбрать'
                recommendation = get_recommendation(sum_for_vocation, city_preference, age, vacation_preference,
                                                    transport_preference, family_members)
                return render_template('where_to_go.html', text_fror_recommendation=text_fror_recommendation,
                                       recommendation=recommendation)
            else:
                return render_template('where_to_go.html',
                                       text_error="Вы не заполнили поля или ввели неверное значение")
        except ValueError:
            return render_template('where_to_go.html', text_error="Вы ввели неверные данные")
    else:
        return render_template('where_to_go.html')


@app.route('/tours', methods=['GET', 'POST'])
def tours():
    if request.method == 'POST':
        try:
            # get user inputs from dropdown menus
            sum_for_tours_from = int(request.form['sum_for_tours_from'])
            sum_for_tours = int(request.form['sum_for_tours'])
            city_preference_tours_from = request.form['city_preference_tours_from']
            city_preference_tours_to = request.form['city_preference_tours_to']
            date_picker = str(request.form['date_picker'])
            if sum_for_tours:
                recommendation_tour = get_recommendation_tours(sum_for_tours_from, sum_for_tours, city_preference_tours_from, city_preference_tours_to, date_picker)
                if recommendation_tour=="error":
                    return render_template('tours.html', error="Извините, ничего не найдено. Попробуйте ещё раз или обратитесь к нам лично.")
                return render_template('tours.html', recommendation=recommendation_tour)
            else:
                return render_template('tours.html',
                                       text_error="Вы не заполнили поля или ввели неверное значение")
        except ValueError:
            return render_template('tours.html', text_error="Вы ввели неверные данные")
    else:
        return render_template('tours.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False)
