import qiling 

"""
Note to run it u need to install qiling framework

visit: https://github.com/qilingframework/qiling for more info


"""




def hyjeck(q1):
    global org_state
    org_state = q1.save()

    function_opcodes = b"\x48\xC7\xC7\x20\x06\x40\x00"
    key_address = 0x40053d
    q1.mem.write(key_address ,function_opcodes)
    q1.reg.rip = 0x400620
    

    
def end_proc(q1):
    q1.emu_stop()
q1 = qiling.Qiling(["./lvl5",  "get_data_addr"], rootfs="/")
q1.hook_address(hyjeck, 0x400520)
q1.hook_address(end_proc,0x004006d6)
q1.filter = "open"
q1.run()




     

