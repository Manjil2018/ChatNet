from flask import Flask ,jsonify, request
from netmiko import Netmiko

app = Flask(__name__)
cisco1 = {
    "host": "192.168.122.10",
    "username": "admin",
    "password": "admin",
    "secret": "admin",
    "device_type": "cisco_ios",
}


@app.route('/getIP' ,  methods=('POST',))
def hello():
    try:
        print(request)
        json_data = request.get_json(force=True)
        print(json_data)
        router_name = json_data['router']
        interface = json_data['interface']
        # get ip from router
        #start for router config

        net_connect = Netmiko(**cisco1)
        command = ("show ip int brief")

        print()
        print(net_connect.find_prompt())
        output = net_connect.send_command(command)
        net_connect.disconnect()
        print(output)

        for single_line in output.splitlines():
           if interface in single_line:
              return single_line

        #end of router add

        #ipadd = "10.20.0.0"
        return jsonify(ip = single_line)

    except Exception as e:
        print(e)
        print("Something went wrong") 
        #print(err)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5050)
