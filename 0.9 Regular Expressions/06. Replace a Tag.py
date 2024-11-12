import re

pattern = r'<a href="([^"]+)">([^<]+)</a>'

while True:
    txt = input()
    if txt == 'end':
        break
    result = re.sub(pattern, r'[URL href="\1"]\2[/URL]', txt)
    print(result)


'''
<ul>
  <li>
    <a href="http://softuni.bg">SoftUni</a>
 </li>
</ul>
end
'''
