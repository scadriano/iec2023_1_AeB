import keyboard

tecla = 0

if (tecla != 1) {

	deuRuim()

}

def deuRuim() {

	while (!keyboard.is_pressed('space')){
		continue
	}
}