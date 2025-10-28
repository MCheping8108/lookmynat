import stun
import easygui

welcome = easygui.buttonbox("你正在使用lookmynat，检测需要10秒左右，请不要关闭此软件", "lookmynat", ["Check NAT"])

checkmynat = stun.get_ip_info()

def your_ip_and_port():
    return f"你的公网IP地址是：{checkmynat[1]}\n\n你的公网端口是：{str(checkmynat[2])}\n\n"

# def CGNAT():
#     if checkmynat[1].startswith("100.") or checkmynat[1].startswith("192.") or checkmynat[1].startswith("172.") or checkmynat[1].startswith("10."):
#         return f"是否存在CGNAT：True\n\n"
#     else:
#         return f"是否存在CGNAT：False\n\n"

if welcome == "Check NAT":
    if checkmynat[0] == 'Full Cone':
        easygui.msgbox(your_ip_and_port() + "NAT类型：Full Cone\n说明：完全锥形NAT，外网主机可以任意发起连接到内网主机", "lookmynat")
    elif checkmynat[0] == 'Restricted Cone':
        easygui.msgbox(your_ip_and_port() + "NAT类型：Restricted Cone\n说明：受限锥形NAT，外网主机只能连接到内网主机曾经发送过数据的外网地址和端口", "lookmynat")
    elif checkmynat[0] == 'Port Restricted Cone':
        easygui.msgbox(your_ip_and_port() + "NAT类型：Port Restricted Cone\n说明：端口受限锥形NAT，外网主机只能连接到内网主机曾经发送过数据的外网地址和端口，并且端口号必须匹配", "lookmynat")
    elif checkmynat[0] == 'Symmetric NAT':
        easygui.msgbox(your_ip_and_port() + "NAT类型：Symmetric NAT\n说明：对称NAT，内网主机每次发送数据到不同的外网地址时，都会分配不同的外网地址和端口", "lookmynat")
