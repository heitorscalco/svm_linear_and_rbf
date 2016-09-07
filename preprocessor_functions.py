class Preprocessor(object):	
	def preprocessing(self, arquivo):

		conjunto_dados = []
		conjunto_resposta = []
		flag = 0
		f = open(arquivo,'r');
		for line in f.xreadlines():
			if (flag==0):				
				num_colunas_arquivo = line.count(',') + 1
				flag = 1
			dados_novos = None;
			dados_novos = [];
			dados =  line.split(",", num_colunas_arquivo); #Separa as linhas por vírgula.
			cont = 0;
			for dado in dados:
				if (cont == 1):	#Ajusta protocolo da camada de transporte.
					dados_novos = self.checkvetor(dados_novos, dado, self.protocolos())
				elif (cont == 2):  #Ajusta servicos
					dados_novos = self.checkvetor(dados_novos, dado, self.servicos())
				elif (cont == 3):  #Ajusta flags.
					dados_novos = self.checkvetor(dados_novos, dado, self.flags())
				elif ((cont == num_colunas_arquivo-1)):
					if (dado == "normal;\n"):
						conjunto_dados.append(dados_novos)
						conjunto_resposta.append(float("+1"))
					else:
						conjunto_dados.append(dados_novos)
						conjunto_resposta.append(float("-1"))
					break
				else:
					dados_novos.append(float(dado))
				cont = cont + 1
		f.close()
		return conjunto_dados, conjunto_resposta


	def checkvetor(self, dados, dado_atual, vetor):
		# TODO quando nao achar aditionar no other
		for dado in vetor:
			if(dado == dado_atual):
				dados.append(1)
			else:
				dados.append(0)
		return dados


	def protocolos(self):
		protocolo = []
		protocolo.append("tcp")
		protocolo.append("udp")
		protocolo.append("icmp")
		protocolo.append("Unknown")
		return protocolo


	def servicos(self):
		servico = []
		servico.append("AUTH")
		servico.append("BGP")
		servico.append("CSNET_NS")
		servico.append("CTF")
		servico.append("DAYTIME")
		servico.append("DISCARD")
		servico.append("DNS")
		servico.append("ECHO")
		servico.append("EFS")
		servico.append("EXEC")
		servico.append("FINGER")
		servico.append("FTP")
		servico.append("FTP-DATA")
		servico.append("GOPHER")
		servico.append("HTTP")
		servico.append("HTTPS")
		servico.append("ICMP")
		servico.append("IMAP4")
		servico.append("IRC")
		servico.append("ISO_TSAP")
		servico.append("KLOGIN")
		servico.append("LDAP")
		servico.append("LINK")
		servico.append("LLMNR")
		servico.append("LOGIN")
		servico.append("NETBIOS_DGM")
		servico.append("NETBIOS_NS")
		servico.append("NETBIOS_SSN")
		servico.append("NETSTAT")
		servico.append("NNTP")
		servico.append("NTP_U")
		servico.append("OTHER")
		servico.append("POP2")
		servico.append("POP3")
		servico.append("PRINTER")
		servico.append("PRIVATE")
		servico.append("REMOTE_JOB")
		servico.append("SMTP")
		servico.append("SPOTIFY")
		servico.append("SQL_NET")
		servico.append("SSDP")
		servico.append("SSH")
		servico.append("SUNRPC")
		servico.append("TELNET")
		servico.append("TFTP_U")
		servico.append("TIME")
		servico.append("URP_I")
		servico.append("UUCP")
		servico.append("UUCP_PATH")
		servico.append("VNC")
		servico.append("VOIP")
		servico.append("WHOIS")
		servico.append("X11")
		servico.append("Z39_50")
		return servico


	def flags(self):
		flag = []
		flag.append("SF")
		flag.append("S1")
		flag.append("REJ")
		flag.append("S2")
		flag.append("S0")
		flag.append("S3")
		flag.append("RSTO")
		flag.append("RSTR")
		flag.append("RSTOS0")
		flag.append("OTH")
		flag.append("SH")
		flag.append("Unknown")
		flag.append("ICMP")
		return flag	