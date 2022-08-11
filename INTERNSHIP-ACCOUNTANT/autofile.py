from docxtpl import DocxTemplate
lock = 1
count=0
while(lock == 1):
    if(count==0):
        initial = input("enter initial:")
        company_name = input("Enter name of the company:")
        owner_initial = input("enter owner initial(MR,MRS):")
        owner = input("enter owner name:")
        role = input("enter role:")
        with open('fav.txt','w') as f_out:
            f_out.write(initial +"\n")
            f_out.write(company_name+"\n")
            f_out.write(owner_initial +"\n")
            f_out.write(owner +"\n")
            f_out.write(role +"\n")
    else:
        with open('fav.txt','r') as f_out:
            values=f_out.read().splitlines()
            initial=values[0]
            company_name=values[1]
            owner_initial=values[2]
            owner=values[3]
            role=values[4]
    date = input("Enter date for appoinment:")
    date1 = input("Enter date for engagement")
    fin_year = input("enter financial year:")
    asses_year = input("enter assessment year:")
    end_year = input("enter end year")
    context = {
    'initial': initial,
    'company_name': company_name,
    'date': date,
    'fin_year': fin_year,
    'ownner_initial': owner_initial,
    'owner_name': owner,
    'role': role,
    'end_year': end_year,
    'date1': date1
    }
    doc1 = DocxTemplate("master_template_assign.docx")
    doc1.render(context)
    doc1.save(asses_year + " "+company_name.upper()+" " +
          "AUDIT" + " "+"APPOINMENT LETTER"+".docx")
    doc2 = DocxTemplate("master_template_engage.docx")
    doc2.render(context)
    doc2.save(asses_year + " "+company_name.upper()+" " +
          "AUDIT" + " "+"ENGAGEMENT LETTER"+".docx")
    lock=int(input("want to continue(1/0)"))
    if lock==0:
        f_out.truncate()
    count=count+1

