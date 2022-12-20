class Rocket():
	def __init__(self, mass, fuel, engine):
		self.mass = mass
		self.fuel = fuel
		engine = engine
		
		
class Vostok(Rocket):
	def __init__(self):
		super().__init__(6750, 2000, True)
		#Проверяет, есть ли топливо в изначально заданных параметрах
		if self.fuel == 0:
			self.engine = False
		else:
			self.engine = True
			#Метод, позволяющий израсходовать count кг топлива
	def spend_fuel(self, count):
		self.fuel = (int(self.fuel) - int(count))
		self.mass = (int(self.mass) - int(count))
		if (int(self.fuel) - int(count)) <= 0:
			self.engine = False
		if self.fuel > 0:
			return True
		else:
			return False
	def get_fuel_level(self):
		return self.fuel
	def get_total_weight(self):
		return(self.mass)
	def get_is_engine_running(self):
		return(self.engine)
		
class main(Rocket):
	def __init__(self):
		super().__init__(int(input()), int(input()), True)
		if self.fuel == 0:
			self.engine = False
		else:
			self.engine = True
		step = int(input())#Количество топлива, тратящегося каждую секунду
		while self.engine == True:#Пока двигатель работает, топливо тратиться
			self.fuel = self.fuel - step
			self.mass = self.mass - step
			if self.fuel - step < 0:
				self.engine = False#Двигатель останавливается, когда топливо кончается
			print(self.mass, self.fuel, self.engine)#Каждый этап выводятся параметры ракеты
			
			
			
	

M = main()
print(M.mass,'\n')

			
		
R = Vostok()

print(R.spend_fuel(2000))
print(R.get_fuel_level())
print(R.get_total_weight())
print(R.get_is_engine_running())
