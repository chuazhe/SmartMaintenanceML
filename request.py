import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={
    "data": [
        {
        	
        	"setting1":2,
        	"setting2":1,
        	"setting3":2,
        	"s1":1,
        	"s2":1,
        	"s3":1,
        	"s4":1,
        	"s5":1,
        	"s6":1,
        	"s7":1,
        	"s8":1,
        	"s9":1,
        	"s10":1,
        	"s11":1,
        	"s12":1,
        	"s13":1,
        	"s14":1,
        	"s15":1,
        	"s16":1,
        	"s17":1,
        	"s18":1,
        	"s19":1,
        	"s20":1,
        	"s21":1

        }
    ]
})

print(r.json())