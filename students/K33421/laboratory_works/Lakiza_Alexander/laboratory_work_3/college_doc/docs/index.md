# Лабораторная работа №3
Реализация серверной части приложения средствами django и djangorestframework

__Вариант 12__  
Создать программную систему, предназначенную для учебной части колледжа.  
Она должна обеспечивать хранение сведений о каждом преподавателе, о
дисциплинах, которые он преподает, номере закрепленного за ним кабинета, о
расписании занятий. Существуют преподаватели, которые не имеют собственного
кабинета.  
О студентах должны храниться следующие сведения: фамилия и имя, в какой
группе учится, какую оценку имеет в текущем семестре по каждой дисциплине.
Замдекана должен иметь возможность добавить сведения о новом преподавателе
или студенте, внести в базу данных семестровые оценки студентов каждой группы по
каждой дисциплине, удалить данные об уволившемся преподавателе и отчисленном из
колледжа студенте, внести изменения в данные об преподавателях и студентах, в том
числе поменять оценку студента по той или иной дисциплине.  
В задачу диспетчера учебной части входит составление расписания.  
Замдекана могут потребоваться следующие сведения:
- Какой предмет будет в заданной группе в заданный день недели на заданном
уроке?
- Кто из преподавателей преподает в заданной группе?
- В каких группах преподает заданный предмет заданный преподаватель?
- Расписание на заданный день недели для указанной группы?
- Сколько студентов обучается на каждом курсе в указанном классе?

Необходимо предусмотреть возможность получения документа,
представляющего собой сводные ведомости успеваемости за семестр по каждой группе.
В ведомости необходимо предусмотреть сведения о среднем балле группы за семестр.