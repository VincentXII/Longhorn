def longhorn():
	import subprocess, sys, os, shutil, platform

	print("""RUN AS ADMIN!!!
		Longhorn CLI v3.0
		By VincentXII
		------------------------------""")
	print("[A] - Remove Default Apps")
	print("[B] - Block Telemetry")
	print("[C] - Remove Cortana")
	print("[D] - Disable Windows Defender")
	print("[I] - Check Windows Info")
	print("[O] - Remove Onedrive")
	print("[RP] - Create Restore Point")
	print("[RS] - Disable Intrusive Services")
	print("[S] - Setup Longhorn")
	print("[U] - Disable Windows Update")
	print("[X] - Exit Longhorn")
	while True:
		choice = input("> ")

		if choice == "A":
			p = subprocess.Popen(["powershell.exe",
				"scripts\\remove-default-apps.ps1"],
				stdout=sys.stdout)
			p.communicate()

		if choice == "B":
			p = subprocess.Popen(["powershell.exe",
				"scripts\\block-telemetry.ps1"],
				stdout=sys.stdout)
			p.communicate()

		if choice == "C":
			p = subprocess.Popen(["scripts\\delCortana.bat"])
			print("Please run [C] twice for it to take full effect.\n")

		if choice == "D":
			p = subprocess.Popen(["powershell.exe",
				"scripts\\disable-windows-defender.ps1"],
				stdout=sys.stdout)
			p.communicate()

		if choice == "I":
			print("----------Windows Info------------")
			import platform as p; print(p.platform());print(p.processor())
			print("----------------------------------")

		if choice == "O": 
			p = subprocess.Popen(["powershell.exe",
	            "scripts\\remove-onedrive.ps1"], 
	            stdout=sys.stdout)
			p.communicate()
		if choice == "RP":
			p = subprocess.Popen(["powershell.exe",
				"scripts\\create-restore-point.ps1"],
				stdout=sys.stdout)
			p.communicate()
		if choice == "RS": 
			p = subprocess.Popen(["powershell.exe",
	            "scripts\\disable-services.ps1"], 
	            stdout=sys.stdout)
			p.communicate()

		if choice == "S":
			p = subprocess.Popen(["powershell.exe",
				'-ExecutionPolicy', 
				'Unrestricted',
	            "scripts\\setup.ps1"], 
	             stdout=sys.stdout)
			p.communicate()

		if choice == "U":
			p = subprocess.Popen(["powershell.exe",
	            "scripts\\disable-windows-update.ps1"], 
	            stdout=sys.stdout)
			p.communicate()

		if choice == "X":
			exit()

		else:
			longhorn()
longhorn()
