import os
filename="student.txt"
def main():
    while True:
        menu()
        choice=int(input("请选择"))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input("您确定要退出程序吗？y/n")
                if answer=="y" or answer=="Y":
                    print("谢谢您的使用!!!")
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()



def menu():
    print("------------------学生信息管理系统----------------------")
    print("---------------------功能菜单------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t\t\t\t\t7.显示所有人员信息")
    print("\t\t\t\t\t\t\t\t\t\t0.退出系统")
    print("--------------------------------------------------------------")

def insert():
    Student_list=[]
    while True:
        id=input("请输入id：")
        if not id:
            break
        try:
            english=int(input("请输入英语成绩："))
            python=int(input("请输入python成绩："))
            java=int(input("请输入java成绩："))
        except:
            print("输入成绩无效，请重新输入")
            continue
        student={"id":id,"English":english,"Python":python,"Java":java}
        Student_list.append(student)
        answer=input("请问还需要添加学生吗？y/n")
        if answer=="y":
            continue
        else:
            break
    save(Student_list)
    print("学生信息储存完毕，感谢你的使用")

def save(lst):
    try:
        stu_text=open(filename,"a",encoding="utf-8")
    except:
        stu_text=open(filename,"w",encoding="utf-8")
    for item in lst:
        stu_text.write(str(item)+"\n")
    stu_text.close()

def search():
    student_query=[]
    while True:
        id=""
        if os.path.exists(filename):
            id=input("请输入你要查询学生的id：")
            with open(filename,"r",encoding="utf-8") as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!="":
                        if d["id"]==id:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                answer=input("是否需要继续查询？y/n")
                if answer=="y":
                    continue
                else:
                    break
        else:
            print('未储存学生信息')
            break

def show_student(lst):
    if len(lst)==0:
        print("没有查询到学生信息，无数据显示！！！")
        return
    format_titile='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t'
    print(format_titile.format("id","英语成绩","python成绩","java成绩","总成绩"))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item.get("id"),
                                 item.get("English"),
                                 item.get("Python"),
                                 item.get("Java"),
                                 int(item.get("English"))+int(item.get("Python"))+int(item.get("Java"))
                                 ))

def delete():
  while True:
    student_id = input("请输入你要删除的id：")
    if student_id != "":
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                student_old = file.readlines()
        else:
            student_old = []
        flag = False
        if student_old:
            with open(filename, "w", encoding="utf-8") as wfile:
                d = {}
                for item in student_old:
                    d = dict(eval(item))
                    if d["id"] != student_id:
                        wfile.write(str(d) + "\n")
                        print(d)
                    else:
                        flag = True
                if flag == True:
                    print(f"id为{student_id}的学生被删除")
                else:
                    print(f"没有找到id为{student_id}的学生")
        else:
            print("没有找到任何学生信息。")
            break
        show()
        answer = input("是否继续删除？y/n")
        if answer == "y":
            continue
        else:
            break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding="utf-8") as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input("请输入你要修改的学生id：")
    with open(filename,"w",encoding="utf-8") as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d["id"]==student_id:
                print("查找到学生信息，可以修改。")
                while True:
                    try:
                        d["English"]=input("重新输入英语成绩")
                        d["Python"]=input("重新输入python成绩")
                        d["Java"]=input("重新输入java成绩")
                        wfile.write(str(d) + "\n")
                        print("修改成功")
                    except:
                        print("输入有误请重新输入")
                    else:
                        break
            else:
                wfile.write(str(d)+"\n")
        answer=input("请问还需要继续修改吗？y/n")
        if answer=="y":
            modify()
        else:
            pass

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
            student_list=rfile.readlines()
            if student_list:
                student_new=[]
                for item in student_list:
                    d=dict(eval(item))
                    student_new.append(d)

            else:
                print("为录入人员信息")

    else:
        print("文件不存在")
    asc_or_des=input("请选择升序还是降序？0/1")
    if asc_or_des=="0":
        asc_or_des_bool=False
    elif asc_or_des=="1":
        asc_or_des_bool=True
    else:
        print("你的输入有误，请重新输入")
        sort()
    mode=input("你选择以哪种方式进行排序，英语，python，还是java？0/1/2")
    if mode=="0":
        student_new.sort(key=lambda x:int(x["English"]),reverse=asc_or_des_bool)
    elif mode=="1":
        student_new.sort(key=lambda x: int(x["Python"]), reverse=asc_or_des_bool)
    elif mode=="2":
        student_new.sort(key=lambda x: int(x["Java"]), reverse=asc_or_des_bool)
    else:
        sort()



def total():
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
            students=rfile.readlines()
            if students:
                print(f"总共由{len(students)}名学生")
            else:
                print("未录入信息")
    else:
        print("文件不存在")
def show():
    stu_lst=[]
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
            students=rfile.readlines()
            if students:
                for item in students:
                    stu_lst.append(eval(item))
            else:
                print("无学生信息")
        show_student(stu_lst)
    else:
        print("为录入任何信息")

if __name__ == '__main__':
    main()
