"""FINDING THE QUANTITY OF CEMENT, SAND AND COURSE AGGREGATE NEEDED FOR A GIVEN VOLUME OF CONCRETE
Assumng density of pcc = 145 lb/ft3 and rcc = 150 lb/ft3
NEED: 
volume of concrete, 
purpose of concrete, 
type of concrete, 
mass ratio of cement, sand and course aggregate"""

wet_vol = int(input('Total volume of concrete needed ( in feet cube):  '))

uses = int(input('What is the purpose: 1 lab or 2 site, just write 1 or 2:  '))
if uses == 1 :
    dry_vol = wet_vol * 1.2
    print (f'we need {dry_vol} feetcube of dry concrete')
elif uses == 2:
    dry_vol = wet_vol * 1.54
    print (f'we need {dry_vol} feetcube of dry concrete')
else:
    print(f'INVALID OPTION SELECTED')

type = int(input('IS it for 1.pcc or 2.rcc, just write 1 or 2 :  '))
""" 
    American standard ACI 318 :
            pcc density=145 lbperftcube and rcc=150
    British standard IS 456:
            pcc density = 24 kN/m3 appr= 150 lb/ft3 and rcc den= 25kN/m3 = 156
    """
if type == 1:
    weight = dry_vol * 145  # unit is lb = ftcubw * lb per ftcube         
elif type == 2:
    weight = dry_vol * 150
print(f'we need {weight} lb of dry mixed concrete')

""" Converting lb to kg"""
masskg = weight * 0.453592375
print(f'we need {masskg:.2f} kg of dry mixed concrete')

# def ratio(cem,san,course):
#     cem
ratio =(input('WHat is the ratio of the concrete needed: cement, sand, course_aggr:\n write in this format 1,2,3 :'))
cem1 = float(ratio[0])
sand1 = float (ratio[2])
ca1 = float(ratio[4])
sum1 = cem1 + sand1 + ca1
cement = cem1/sum1* masskg 
sand = sand1/sum1* masskg
course = ca1/sum1 *masskg
print(f'We need {cement:.2f} kg of cement, {sand:.2f} kg of sand, and {course:.2f} kg of course aggregate')
