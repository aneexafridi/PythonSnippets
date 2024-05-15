class Password:
	pass_word = 10
	@classmethod
	def Value(self):
		print("Class Variable: ",self.pass_word)

A = Password()
B = Password()
C = Password()

A.Value()
B.pass_word = 99

print(A.pass_word)
print(B.pass_word)
print(C.pass_word)