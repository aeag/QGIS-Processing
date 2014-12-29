##Table=group
##layer_input=vector
##outputfile=output html
import qgis.utils

try: 
    import pandas as pd
    import numpy as np
except:
    print 'pandas and numpy library could not be loaded. Install process is described here kkkkkk'
    
import sys
reload(sys)  
sys.setdefaultencoding('UTF8')

progress.setInfo(u'\n --- Describe data algorithm started--- \n')

html_header = str("""<html>
<head>
<meta charset="UTF-8">
<style>
table {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    font-size: .7em;
    width: 100%;
    border-collapse: collapse;
}
table td,  th {
    font-size: .8em;
    border: 1px solid #98bf21;
    padding: 3px 7px 2px 7px;
}
table th {
    font-size: .8m;
    text-align: left;
    padding-top: 5px;
    padding-bottom: 4px;
    background-color: #A7C942;
    color: #ffffff;
}
 table tr.alt td {field_names
    color: #000000;field_names
    background-color: #EAF2D3;
}
</style>
</head>
<body>
""")
    
layer = processing.getObject(layer_input)

fields = layer.pendingFields()
field_names = [field.name() for field in fields]
fieldsDesc = [u'Fields:'] 


# describe table fields
for field in fields:
    fileinfo= u"<b>- %s Type:</b> %s, Length: %s " % ( field.name(), field.typeName(), field.length())
    fieldsDesc.append(fileinfo)

html_fields = (u'<br> '.join(fieldsDesc))

attr = []
for elem in layer.getFeatures(): ##Table=group
##layer_input=vector
##outputfile=output html
import qgis.utils

try: 
    import pandas as pd
    import numpy as np
except:
    print 'pandas and numpy library could not be loaded. Install process is described here kkkkkk'
    
import sys
reload(sys)  
sys.setdefaultencoding('UTF8')

progress.setInfo(u'\n --- Describe data algorithm started--- \n')

html_header = str("""<html>
<head>
<meta charset="UTF-8">
<style>
table {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    font-size: .7em;
    width: 100%;
    border-collapse: collapse;
}
table td,  th {
    font-size: .8em;
    border: 1px solid #98bf21;
    padding: 3px 7px 2px 7px;
}
table th {
    font-size: .8m;
    text-align: left;
    padding-top: 5px;
    padding-bottom: 4px;
    background-color: #A7C942;
    color: #ffffff;
}
 table tr.alt td {field_names
    color: #000000;field_names
    background-color: #EAF2D3;
}
</style>
</head>
<body>
""")
    
layer = processing.getObject(layer_input)

fields = layer.pendingFields()
field_names = [field.name() for field in fields]
fieldsDesc = [u'Fields:'] 


# describe table fields
for field in fields:
    fileinfo= u"<b>- %s Type:</b> %s, Length: %s " % ( field.name(), field.typeName(), field.length())
    fieldsDesc.append(fileinfo)

html_fields = (u'<br> '.join(fieldsDesc))

attr = []
for elem in layer.getFeatures(): 
    attr.append(elem.attributes())
    #  if contains text for all columns auto switches to text stats
df = pd.DataFrame(data=attr, columns = field_names)
summary = ['<p> Table stats ']
summary.append(df.describe(include='all').to_html().rstrip('\r\n'))
summary.append('</p>')

head = df.head()

 
html_tab_summary=''.join(summary)

html_tab_head=''.join(head.to_html().rstrip('\r\n'))
html_tab_head = html_tab_head + u'<br>      ...  '


html_result = html_header + html_fields + u'<p>' + html_tab_summary + u"</p> <p>" +html_tab_head +u"</p>" + u"</body></html>" 
f = open(outputfile, 'a')
f.close
f.write(html_result.encode('utf8'))
    attr.append(elem.attributes())
    #  if contains text for all columns auto switches to text stats
df = pd.DataFrame(data=attr, columns = field_names)
summary = ['<p> Table stats ']
summary.append(df.describe(include='all').to_html().rstrip('\r\n'))
summary.append('</p>')

head = df.head()

 
html_tab_summary=''.join(summary)

html_tab_head=''.join(head.to_html().rstrip('\r\n'))
html_tab_head = html_tab_head + u'<br>      ...  '


html_result = html_header + html_fields + u'<p>' + html_tab_summary + u"</p> <p>" +html_tab_head +u"</p>" + u"</body></html>" 
f = open(outputfile, 'a')
f.close
f.write(html_result.encode('utf8')) 
