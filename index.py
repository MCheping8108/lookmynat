import stun
import easygui

welcome = easygui.buttonbox("你正在使用lookmynat，检测需要10秒左右，请不要关闭此软件", "lookmynat", ["Check NAT"])

checkmynat = stun.get_ip_info()

if welcome == "Check NAT":
    easygui.msgbox("你的NAT类型是：" + checkmynat[0] +
                   "\n你的IP地址是：" + checkmynat[1] +
                   "\n你的端口是：" + str(checkmynat[2]))

