import pyshark

capture =  pyshark.FileCapture('traffic_capture.pcap')
for i,packet in enumerate(capture):
	if i == 1:
		print(packet.__dict__)
		print(dir(packet))
		print(packet.eth.__dict__)
		print(packet.ip.__dict__)
		print(packet.eth)
		print(packet.ip)
		print(packet.frame_info)
		print(packet.tcp)
		print(packet.length)
		break
