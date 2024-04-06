# # from flask import Flask, request, jsonify
# # import question_book as qb
# # app = Flask(__name__)



# # current_question_index = 0

# # @app.route('/ask', methods=['GET', 'POST'])
# # def ask_question():
# #     global current_question_index
# #     if request.method == 'POST':
# #         user_response = request.json.get('response')
# #         print(user_response)
# #         current_question_index = int(user_response)
# #         if current_question_index < len(qb.questions):
# #             next_question = qb.questions[current_question_index][0]
# #             subject=qb.questions[current_question_index][1]
# #             return jsonify({'question': next_question,
# #                             'subject':subject})
# #         else:
# #             return jsonify({'question': 'Bye! You answered all the questions.',
# #                             'subject':"pass"})
# #     return jsonify({'question': qb.questions[current_question_index],
# #                     'subject':"pass"})

# # if __name__ == '__main__':
# #     app.run(debug=True)

from flask import Flask, request, jsonify
# from flask_cors import CORS  # Import CORS from flask_cors
import question_book as qb
import random

app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes in your Flask app

current_question_index = 0

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    global current_question_index
    if request.method == 'POST':
        user_response = request.json.get('response')
        print(user_response)
        current_question_index = int(user_response)
        if current_question_index < len(qb.questions):
            next_question = qb.questions[current_question_index][0]
            subject=qb.questions[current_question_index][1]
            return jsonify({'question': next_question, 'subject': subject})
        else:
            return jsonify({'question': 'Bye! You answered all the questions.', 'subject': "pass"})
    return jsonify({'question': qb.questions[current_question_index], 'subject': "pass"})

# if __name__ == '__main__':
#     app.run(debug=True)

##################################################################################

maths=0
bio=0
lang=0
chem=0
phy=0
drawing =0
handicap=0
ss=0
intrest1=""
intrest2=""

#####################################  Lists  ######################################

arts = [
    ["Do you enjoy expressing yourself creatively through art, writing, or performance?", 'Arts and Humanities'],
    ["Are you interested in learning about different cultures and historical periods?", 'Arts and Humanities'],
    ["Would you like to pursue a career in fields like literature, fine arts, or theater?", 'Arts and Humanities'],
    ["Do you have a passion for storytelling and communicating ideas through various mediums?", 'Arts and Humanities'],
    ["Are you open to exploring unconventional career paths in creative industries?", 'Arts and Humanities'],
    ["Do you see yourself thriving in environments where you can collaborate with other artists and professionals?", 'Arts and Humanities'],
    ["Are you willing to take risks and embrace failure as part of the creative process?", 'Arts and Humanities'],
    ["Do you enjoy analyzing and critiquing works of art, literature, or film?", 'Arts and Humanities'],
    ["Are you interested in exploring careers that require strong communication and presentation skills?", 'Arts and Humanities'],
    ["Do you see yourself making a living doing something you're passionate about in the arts and humanities field?", 'Arts and Humanities']
]
business = [
    ["Are you interested in learning about how businesses operate and succeed in competitive markets?", 'Business and Entrepreneurship'],
    ["Do you enjoy taking initiative and pursuing opportunities for innovation and growth?", 'Business and Entrepreneurship'],
    ["Are you comfortable with taking calculated risks and managing uncertainties in business ventures?", 'Business and Entrepreneurship'],
    ["Would you like to pursue a career as an entrepreneur, business owner, or corporate leader?", 'Business and Entrepreneurship'],
    ["Do you have strong analytical and problem-solving skills for identifying market trends and strategic opportunities?", 'Business and Entrepreneurship'],
    ["Are you interested in learning about different aspects of business management, such as marketing, finance, or operations?", 'Business and Entrepreneurship'],
    ["Are you willing to invest time and resources into developing your business ideas and concepts?", 'Business and Entrepreneurship'],
    ["Do you see yourself building networks and partnerships to support your entrepreneurial endeavors?", 'Business and Entrepreneurship'],
    ["Are you open to learning from failures and setbacks to iterate and improve your business strategies?", 'Business and Entrepreneurship'],
    ["Do you have the ambition and determination to pursue your entrepreneurial dreams despite challenges and obstacles?", 'Business and Entrepreneurship']
]
ca_questions = [
    ["Are you passionate about accounting principles, taxation, and auditing practices?", 'Chartered Accountancy (CA)'],
    ["Do you enjoy working with numbers and ensuring accuracy in financial records and statements?", 'Chartered Accountancy (CA)'],
    ["Are you willing to commit to a rigorous and demanding course of study to become a qualified CA?", 'Chartered Accountancy (CA)'],
    ["Would you like to pursue a career that involves providing financial advice, auditing services, or tax planning for clients?", 'Chartered Accountancy (CA)'],
    ["Are you comfortable with the responsibilities and ethical considerations associated with handling sensitive financial information?", 'Chartered Accountancy (CA)'],
    ["Do you have strong attention to detail and the ability to spot discrepancies or irregularities in financial documents?", 'Chartered Accountancy (CA)'],
    ["Are you interested in gaining practical experience through internships or apprenticeships in accounting firms or corporate finance departments?", 'Chartered Accountancy (CA)'],
    ["Do you see yourself pursuing additional certifications or specializations to enhance your expertise in accounting and finance?", 'Chartered Accountancy (CA)'],
    ["Are you open to continuous learning and staying updated on changes in accounting standards, tax regulations, and financial reporting requirements?", 'Chartered Accountancy (CA)'],
    ["Are you willing to invest time and resources into developing your business ideas and concepts?", 'Chartered Accountancy (CA)'],]
commerce = [
    ["Are you interested in learning about business transactions, finance, and economics?", 'Commerce'],
    ["Do you enjoy analyzing data and financial statements to understand the performance of businesses?", 'Commerce'],
    ["Are you curious about how markets function and the factors that influence supply and demand?", 'Commerce'],
    ["Would you like to pursue a career in fields such as accounting, finance, or business management?", 'Commerce'],
    ["Are you comfortable with mathematical concepts and calculations required for financial analysis?", 'Commerce'],
    ["Do you have strong analytical and problem-solving skills for interpreting complex business scenarios?", 'Commerce'],
    ["Are you willing to keep up with changes in tax laws, regulations, and financial reporting standards?", 'Commerce'],
    ["Do you see yourself working in roles such as financial analyst, auditor, or investment banker?", 'Commerce'],
    ["Are you interested in exploring opportunities for internships or work experience in accounting firms or financial institutions?", 'Commerce'],
    ["Do you have the ambition and drive to excel in a career that involves managing financial resources and advising businesses?", 'Commerce']
]
eng = [
    ["Are you interested in learning how machines work and how to design them?", 'Engineering and Technology'],
    ["Do you enjoy working with computers and exploring new software applications?", 'Engineering and Technology'],
    ["Are you curious about how technology can be used to solve real-world problems?", 'Engineering and Technology'],
    ["Would you like to explore careers in fields like robotics, aerospace, or software development?", 'Engineering and Technology'],
    ["Are you comfortable with mathematical concepts and analytical thinking required for engineering?", 'Engineering and Technology'],
    ["Do you enjoy building things and experimenting with different materials and designs?", 'Engineering and Technology'],
    ["Are you interested in learning coding languages to create websites or software programs?", 'Engineering and Technology'],
    ["Would you like to work in a field where you can contribute to advancements in technology and innovation?", 'Engineering and Technology'],
    ["Are you willing to pursue further education or certifications to specialize in a specific area of engineering?", 'Engineering and Technology'],
    ["Do you see yourself enjoying a career where you can apply scientific principles to practical solutions?", 'Engineering and Technology']
]
law = [
    ["Are you interested in understanding how laws are created and enforced in society?", 'Law and Legal Studies'],
    ["Do you enjoy debating and analyzing complex issues from different perspectives?", 'Law and Legal Studies'],
    ["Are you interested in learning about the principles of justice and ethics?", 'Law and Legal Studies'],
    ["Would you like to pursue a career as a lawyer, judge, or legal consultant?", 'Law and Legal Studies'],
    ["Do you have strong critical thinking and research skills required for legal analysis?", 'Law and Legal Studies'],
    ["Are you comfortable with public speaking and presenting arguments in front of others?", 'Law and Legal Studies'],
    ["Are you willing to dedicate several years to education and training to become a legal professional?", 'Law and Legal Studies'],
    ["Are you interested in exploring various areas of law, such as criminal law, civil law, or international law?", 'Law and Legal Studies'],
    ["Do you see yourself advocating for the rights of individuals and marginalized communities through legal practice?", 'Law and Legal Studies'],
    ["Do you have the integrity and commitment to uphold the principles of justice and fairness in your work?", 'Law and Legal Studies']
]
medicine = [
    ["Are you passionate about helping people and improving their health and well-being?", 'Medicine and Healthcare'],
    ["Are you comfortable with the idea of working in environments like hospitals or clinics?", 'Medicine and Healthcare'],
    ["Do you have a strong stomach and are not easily squeamish around blood or bodily fluids?", 'Medicine and Healthcare'],
    ["Are you interested in learning about human anatomy, physiology, and diseases?", 'Medicine and Healthcare'],
    ["Would you like to pursue a career that involves continuous learning and keeping up with advancements in medical science?", 'Medicine and Healthcare'],
    ["Do you have good communication skills and enjoy interacting with patients and their families?", 'Medicine and Healthcare'],
    ["Are you willing to dedicate several years to education and training to become a healthcare professional?", 'Medicine and Healthcare'],
    ["Are you interested in exploring different healthcare fields, such as nursing, physical therapy, or medical research?", 'Medicine and Healthcare'],
    ["Do you have the resilience and emotional intelligence to handle the challenges of working in healthcare?", 'Medicine and Healthcare'],
    ["Do you see yourself making a positive impact on people's lives through a career in medicine or healthcare?", 'Medicine and Healthcare']
]
psycho = [
    ["Are you fascinated by human behavior and the workings of the mind?", 'Psychology and Counseling'],
    ["Do you enjoy helping others navigate through challenges and improve their mental well-being?", 'Psychology and Counseling'],
    ["Are you empathetic and nonjudgmental towards people's experiences and emotions?", 'Psychology and Counseling'],
    ["Would you like to pursue a career as a psychologist, counselor, or therapist?", 'Psychology and Counseling'],
    ["Do you have strong listening and communication skills for building trust and rapport with clients?", 'Psychology and Counseling'],
    ["Are you interested in learning about various therapeutic approaches and interventions for supporting individuals' mental health?", 'Psychology and Counseling'],
    ["Are you willing to pursue advanced education and licensure requirements for practicing psychology or counseling?", 'Psychology and Counseling'],
    ["Do you see yourself working in diverse settings such as schools, clinics, or private practices to serve different populations?", 'Psychology and Counseling'],
    ["Are you committed to ongoing self-reflection and professional development to enhance your counseling skills?", 'Psychology and Counseling'],
    ["Do you have the resilience and self-care practices to manage the emotional demands of working in mental health professions?", 'Psychology and Counseling']
]
sports_questions = [
    ["Are you passionate about playing sports and staying physically active?", 'Sports and Athletics'],
    ["Do you enjoy working as part of a team towards a common goal?", 'Sports and Athletics'],
    ["Are you interested in learning about sports science and training techniques to improve performance?", 'Sports and Athletics'],
    ["Would you like to pursue a career as a professional athlete, coach, or sports therapist?", 'Sports and Athletics'],
    ["Do you have the discipline and dedication to maintain a rigorous training regimen?", 'Sports and Athletics'],
    ["Are you comfortable with the competitive nature of sports and the possibility of facing setbacks and injuries?", 'Sports and Athletics'],
    ["Are you interested in exploring different sports and finding one that aligns with your strengths and interests?", 'Sports and Athletics'],
    ["Do you see yourself inspiring others through your achievements and dedication to sports?", 'Sports and Athletics'],
    ["Are you willing to pursue opportunities for scholarships or sponsorships to support your athletic pursuits?", 'Sports and Athletics'],
    ["Do you have the resilience and determination to overcome challenges and pursue excellence in sports?", 'Sports and Athletics']
]
teaching = [
    ["Are you passionate about working with children or young adults?", 'Education and Teaching'],
    ["Do you enjoy sharing knowledge and helping others learn?", 'Education and Teaching'],
    ["Are you patient and empathetic towards diverse learners' needs?", 'Education and Teaching'],
    ["Would you like to pursue a career as a teacher, instructor, or education administrator?", 'Education and Teaching'],
    ["Do you have strong communication and interpersonal skills for engaging with students and parents?", 'Education and Teaching'],
    ["Are you interested in learning about educational theories and teaching methods?", 'Education and Teaching'],
    ["Are you willing to pursue further education and training, such as a teaching certification or graduate degree in education?", 'Education and Teaching'],
    ["Do you see yourself making a positive impact on students' lives through teaching and mentoring?", 'Education and Teaching'],
    ["Are you open to adapting teaching strategies to accommodate different learning styles and abilities?", 'Education and Teaching'],
    ["Do you have a passion for fostering a supportive and inclusive learning environment in the classroom?", 'Education and Teaching']
]
tour = [
    ["Are you passionate about providing excellent customer service and creating memorable experiences for others?", 'Hospitality and Tourism'],
    ["Do you enjoy working in fast-paced environments and interacting with people from diverse backgrounds?", 'Hospitality and Tourism'],
    ["Are you interested in learning about different cultures, cuisines, and travel destinations?", 'Hospitality and Tourism'],
    ["Would you like to pursue a career in hospitality management, hotel administration, or tourism marketing?", 'Hospitality and Tourism'],
    ["Do you have strong interpersonal and communication skills required for working in the hospitality industry?", 'Hospitality and Tourism'],
    ["Are you comfortable with multitasking and problem-solving in dynamic situations?", 'Hospitality and Tourism'],
    ["Are you interested in exploring opportunities for internships or part-time jobs in hotels, restaurants, or travel agencies?", 'Hospitality and Tourism'],
    ["Do you see yourself thriving in roles that involve coordinating events, managing accommodations, or organizing travel itineraries?", 'Hospitality and Tourism'],
    ["Are you willing to adapt to changing trends and technologies in the hospitality and tourism sectors?", 'Hospitality and Tourism'],
    ["Do you have a passion for creating positive experiences and ensuring customer satisfaction in the hospitality industry?", 'Hospitality and Tourism']
]

sets_to_be_included=[arts,business,ca_questions,commerce,eng,law,medicine,psycho,sports_questions,teaching,tour]


def questionsToBeAsked():
    if(maths<75):
        if(eng in sets_to_be_included):
            sets_to_be_included.remove(eng)
        if(ca_questions in sets_to_be_included):
            sets_to_be_included.remove(ca_questions)

    if(phy<75):
        if(eng in sets_to_be_included):
            sets_to_be_included.remove(eng)

    # if(chem<60):
    #     if("phar-diet-physio-dentist" in sets_to_be_included):
    #         sets_to_be_included.remove("phar-diet-physio-dentist")
    #     if("chem-civil" in sets_to_be_included):
    #         sets_to_be_included.remove("chem-civil")

    if(bio<60):
        if(medicine in sets_to_be_included):
            sets_to_be_included.remove(medicine)

    if(bio<75):
        if(medicine in sets_to_be_included):
            sets_to_be_included.remove(medicine)
    
    # if(lang<70):
    #     if("adv-journal" in sets_to_be_included):
    #         sets_to_be_included.remove("adv-journal")
    #     if("air-hostess" in sets_to_be_included):
    #         sets_to_be_included.remove("air-hostess")

    if(ss<70):
        if(law in sets_to_be_included):
            sets_to_be_included.remove(law)
    
    if(handicap==1):
        if(sports_questions in sets_to_be_included):
            sets_to_be_included.remove(sports_questions)


    if(eval(intrest1) in sets_to_be_included):
        sets_to_be_included.remove(eval(intrest1))
    if(eval(intrest2) in sets_to_be_included):
        sets_to_be_included.remove(eval(intrest2))

    # if(drawing==0):
    #     if("anim-archi-fd" in sets_to_be_included):
    #         sets_to_be_included.remove("anim-archi-fd")
       

def framingQuestions():
    qb.questions.clear()
    for lst in sets_to_be_included:
        for ques in lst:
            qb.questions.append(ques)

    if(intrest1 !=intrest2):
        for i in range(5,10):
            qb.questions.insert(0,eval(intrest1)[i])
            qb.questions.insert(0,eval(intrest2)[i])
    random.shuffle(qb.questions)

    if(intrest1 !=intrest2):
        for i in range(5):
            qb.questions.insert(0,eval(intrest1)[i])
            qb.questions.insert(0,eval(intrest2)[i])
    else:
        for i in range(5):
            qb.questions.insert(0,eval(intrest1)[i])
    



        



####################################################################################
@app.route('/takemarks', methods=['POST'])
def takemarks():
    # Get data from request body
    data = request.get_json()

    # Check if all required fields are present in the request
    required_fields = ['math', 'phy', 'chem', 'bio', 'ss', 'lang', 'drawing','handicap','intrest1','intrest2']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Calculate total score
    print("maths : "+str(data['math']))
    print("chem : "+str(data['chem']))
    global maths,bio,phy,lang,chem,ss,drawing,handicap,intrest1,intrest2
    maths=data['math']
    chem=data['chem']
    bio=data['bio']
    phy=data['phy']
    ss=data['ss']
    lang=data['lang']
    drawing=data['drawing']
    handicap=data['handicap']
    intrest1=data['intrest1']
    intrest2=data['intrest2']
    questionsToBeAsked()
    framingQuestions()
    # total_score = sum(data[field] for field in required_fields)
    print(len(qb.questions))
    

    # Return total score as JSON response
    return jsonify({'total_score': "Got your marks"})

if __name__ == '__main__':
    app.run(debug=True)
