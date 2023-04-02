# Modo 1 -> Sem Init

class MeuNumero():
	
	def Dobro(num):
		return num*2
	
	def Quadrado(num):
		return num*num
	
	def Metade(num):
		return num / 2 if num!=0 else 0

# Modo 2 -> Com Init

class MeuTexto():
	
	def ___init__(self, nome, sobrenome):
		self.fn = nome
		self.ln = sobrenome

	def Maiuscula(self):
		return f'{self.fn} {self.ln}'.upper()

	def Minuscula(self):
		return f'{self.fn} {self.ln}'.lower()

	

