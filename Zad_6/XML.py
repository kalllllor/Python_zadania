from xml.dom import minidom

domtree = minidom.parse("Books.xml")
menu = domtree.documentElement

Books = menu.getElementsByTagName('Book')

for element in Books: 
    if element.hasAttribute('id'):
         print("ID: {}".format(element.getAttribute('id')))

    print("Author: {}".format(element.getElementsByTagName('Author')[0].childNodes[0].data))
    print("Title: {}".format(element.getElementsByTagName('Title')[0].childNodes[0].data))
    print("Genre: {}".format(element.getElementsByTagName('Genre')[0].childNodes[0].data))
    print("Price: {}".format(element.getElementsByTagName('Price')[0].childNodes[0].data))

Books[1].getElementsByTagName('Price')[0].childNodes[0].nodeValue = 30
domtree.writexml(open('BooksChanged.xml', 'w'))
