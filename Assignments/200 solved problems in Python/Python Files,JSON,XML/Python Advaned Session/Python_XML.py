import xml.etree.ElementTree as ET

xmlFile = "D:\\Testing\\Python Advaned Session\\Data\\EmployeeDetails.xml"

# #Example 1(a) : Parsing the XML string
# xmlString = '<employeeDetails><employee><name>Maruthi</name><empID>23678</empID><doj>25-Aug-2018</doj></employee></employeeDetails>'
# xmlTree = ET.fromstring(xmlString)
# print("From String : ", xmlTree) 

# #Example 1(b) : Parsing the XML File 
xmlTree = ET.parse(xmlFile)
# print("From File : ", xmlTree)

# # # #Example 2 : Getting the Root Element of the tree
root = xmlTree.getroot()
print(root)

# # #Example 3 : Reading the attributes for a node 
# # #Root Attributes - Returns a dictionary of attributes and value
# # #so we can set/get the attributes like dictionary
# attributes = root.attrib
# print(attributes)

# # #Example 4 : Identifying the child nodes
# # #Method 1: 
for child in root:
	print(child) 


# #Method 2: 
# for employee in root.iter('employee'):
# 	# print (employee)
# 	print ("Tag : ", employee.tag)
	# for details in employee:
	# 	print ("Node Name : ",details.tag,"\n Node Value : ", details.text)


# #Example 5 : Modifying the xml 
# for employee in root.iter('employee'):
# 	if employee[0].text == "Balaji":
# 		dependants = employee.find('dependants').text
# 		print ("**",dependants)
# 		employee.find('dependants').text = "Suhail" #Modify the value of a node
# 		employee.find('dependants').set("purpose","medical benefits") #Modify the attribute for a node
		
# xmlTree.write("OutputFile.xml")


# #Example 6 : Creating XML 
# #Update the same XML 
# #Say, we would like to add an employee to the xml
# #Details : Name = "Maruthi" EmpID = "23678" DOJ=25-Aug-2018 

# node = ET.Element("employee")
# root.append(node)

# details = ET.SubElement(node, "name")
# details.text = "Maruthi"
# details = ET.SubElement(node, "empID")
# details.text = "23678"
# details = ET.SubElement(node, "doj")
# details.text = "25-Aug-2018"

# xmlTree.write("D:\\Testing\\Python Advaned Session\\Data\\Example60.xml")

# #Example 7 : Create a new xml File 
# #Step1 : Create a root 
# root = ET.Element("employeeDeatils")
# tree = ET.ElementTree(root)

# node = ET.Element("employee")
# root.append(node)

# details = ET.SubElement(node, "name")
# details.text = "Maruthi"
# details = ET.SubElement(node, "empID")
# details.text = "23678"
# details = ET.SubElement(node, "doj")
# details.text = "25-Aug-2018"

# root.append(node)

# details = ET.SubElement(node, "name")
# details.text = "Suhail"
# details = ET.SubElement(node, "empID")
# details.text = "236781"
# details = ET.SubElement(node, "doj")
# details.text = "25-Aug-2019"

# tree.write("D:\\Testing\\Python Advaned Session\\Data\\Example601.xml")


# print (ET.tostring(root))
# xmlFile = "D:\\Testing\\Python Advaned Session\\Data\\Example601.xml"
# xmlTree = ET.parse(xmlFile)
# root = xmlTree.getroot()
# for employee in root.iter('employee'):
# 	print (employee)
# 	print ("Tag : ", employee.tag)
# 	for details in employee:
# 		print ("Node Name : ",details.tag,"\n Node Value : ", details.text)