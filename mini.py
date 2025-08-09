#!/usr/bin/env python3
AA='normal'
A9='Ошибка'
A8='russian'
A7='voices'
A6='C:\\vosk'
A5='maxOutputChannels'
A4='maxInputChannels'
A3='Предупреждение'
A2='vertical'
A1='Применить'
A0='О программе'
z='Аудио устройства'
y='пока'
x='quit'
w='stop'
v='exit'
u='завершить'
t='стоп'
s='выход'
r=enumerate
q=float
p=isinstance
o=AttributeError
n=TypeError
m=range
i='volume'
h='selected_output'
g='selected_input'
f='log_options'
e='exit_commands'
d='tts_rate'
c='both'
b='disabled'
a='bold'
Z='w'
Y='show_ready_messages'
X='show_exit_commands'
W='show_timestamp'
V=any
U=getattr
S='name'
R='rate'
Q=len
N='speech_recognition'
L='left'
J='tts_details'
I='audio_connections'
H=True
G=Exception
F=None
C='Arial'
E='debug_info'
D=False
B='device_info'
import os,sys,json as O,time as P,threading as T,tkinter as A
from tkinter import ttk,messagebox as K,Menu as M
import pyaudio as j,pyttsx3 as k,vosk as l,wave,io
class AB:
	def __init__(C,root):C.root=root;C.root.title('Голосовой Эхо-Ассистент');C.root.geometry('400x120');C.root.resizable(D,D);C.audio=F;C.vosk_model=F;C.vosk_rec=F;C.tts_engine=F;C.is_listening=D;C.listen_thread=F;C.tts_busy=D;C.speech_counter=0;C.tts_rate=A.IntVar(value=150);C.log_options={B:A.BooleanVar(value=D),N:A.BooleanVar(value=H),J:A.BooleanVar(value=D),I:A.BooleanVar(value=D),E:A.BooleanVar(value=D),W:A.BooleanVar(value=D),X:A.BooleanVar(value=D),Y:A.BooleanVar(value=D)};C.exit_commands=[s,t,u,v,w,x,y];C.input_devices=[];C.output_devices=[];C.selected_input=A.StringVar();C.selected_output=A.StringVar();C.settings_file='settings.json';C.load_settings();C.create_menu();C.create_widgets();C.init_audio_system()
	def create_menu(A):G=M(A.root);A.root.config(menu=G);D=M(G,tearoff=0);G.add_cascade(label='Настройки',menu=D);F=M(D,tearoff=0);D.add_cascade(label='Скорость произношения',menu=F);F.add_command(label='Медленно (75)',command=lambda:A.set_speed(75));F.add_command(label='Нормально (150)',command=lambda:A.set_speed(150));F.add_command(label='Быстро (225)',command=lambda:A.set_speed(225));F.add_separator();F.add_command(label='Настроить...',command=A.open_speed_dialog);H=M(D,tearoff=0);D.add_cascade(label=z,menu=H);H.add_command(label='Обновить список',command=A.refresh_devices);H.add_command(label='Показать все устройства',command=A.show_all_devices);C=M(D,tearoff=0);D.add_cascade(label='Что выводить в лог',menu=C);C.add_checkbutton(label='❌ Информация об устройствах',variable=A.log_options[B],command=A.save_settings);C.add_checkbutton(label='✓ Распознавание речи',variable=A.log_options[N],command=A.save_settings);C.add_checkbutton(label='❌ Подробности TTS',variable=A.log_options[J],command=A.save_settings);C.add_checkbutton(label='❌ Подключения аудио',variable=A.log_options[I],command=A.save_settings);C.add_checkbutton(label='❌ Отладочная информация',variable=A.log_options[E],command=A.save_settings);C.add_separator();C.add_checkbutton(label='❌ Показывать время [15:00:49]',variable=A.log_options[W],command=A.save_settings);C.add_checkbutton(label='❌ Показывать "Команда выхода распознана в:"',variable=A.log_options[X],command=A.save_settings);C.add_checkbutton(label='❌ Показывать "ГОТОВО #266 за 4.31с:"',variable=A.log_options[Y],command=A.save_settings);D.add_separator();D.add_command(label='Настроить голосовые команды',command=A.open_voice_commands_dialog);K=M(G,tearoff=0);G.add_cascade(label='Справка',menu=K);K.add_command(label=A0,command=A.show_about)
	def create_widgets(B):H='white';G='<<ComboboxSelected>>';F='readonly';D=A.LabelFrame(B.root,text=z,font=(C,10));D.pack(pady=5,padx=15,fill='x');A.Label(D,text='Микрофон:',font=(C,9)).grid(row=0,column=0,sticky=Z,padx=5,pady=2);B.input_combo=ttk.Combobox(D,textvariable=B.selected_input,state=F,width=32,font=(C,8));B.input_combo.grid(row=0,column=1,padx=5,pady=2);B.input_combo.bind(G,lambda event:B.save_settings());A.Label(D,text='Динамики:',font=(C,9)).grid(row=1,column=0,sticky=Z,padx=5,pady=2);B.output_combo=ttk.Combobox(D,textvariable=B.selected_output,state=F,width=32,font=(C,8));B.output_combo.grid(row=1,column=1,padx=5,pady=2);B.output_combo.bind(G,lambda event:B.save_settings());E=A.Frame(B.root);E.pack(pady=5);B.start_btn=A.Button(E,text='Начать слушать',command=B.start_listening,bg='#4CAF50',fg=H,font=(C,10,a),width=15,height=1);B.start_btn.pack(side=L,padx=5,pady=2);B.stop_btn=A.Button(E,text='Остановить',command=B.stop_listening,bg='#f44336',fg=H,font=(C,10,a),width=15,height=1,state=b);B.stop_btn.pack(side=L,padx=5,pady=2)
	def update_window_title(A,status):A.root.title(f"Голосовой Эхо-Ассистент - {status}")
	def set_speed(A,speed):
		C=speed;A.tts_rate.set(C)
		if A.tts_engine is not F:
			try:A.tts_engine.setProperty(R,C);A.log_message(f"Скорость изменена на: {C}",B);A.save_settings()
			except G as D:A.log_message(f"Ошибка изменения скорости: {D}",E)
	def open_speed_dialog(E):
		B=A.Toplevel(E.root);B.title('Настройка скорости');B.geometry('300x120');B.resizable(D,D);B.transient(E.root);B.grab_set();A.Label(B,text='Скорость произношения:',font=(C,10)).pack(pady=5);F=A.IntVar(value=E.tts_rate.get());G=A.Scale(B,from_=50,to=300,orient='horizontal',variable=F,length=250);G.pack(pady=5);A.Label(B,text='50=медленно  150=нормально  300=быстро',font=(C,8),fg='gray').pack()
		def H():E.set_speed(F.get());B.destroy()
		A.Button(B,text=A1,command=H,bg='lightblue').pack(pady=5)
	def open_voice_commands_dialog(E):
		M='\n';I='1.0';F=A.Toplevel(E.root);F.title('Настройка голосовых команд выхода');F.geometry('450x300');F.resizable(D,D);F.transient(E.root);F.grab_set();A.Label(F,text='Слова и фразы для остановки программы:',font=(C,12,a)).pack(pady=10);A.Label(F,text='(Каждое слово или фразу с новой строки)',font=(C,9),fg='gray').pack();J=A.Frame(F);J.pack(pady=10,padx=20,fill=c,expand=H);E.commands_text=A.Text(J,height=10,width=50,font=(C,10));N=A.Scrollbar(J,orient=A2,command=E.commands_text.yview);E.commands_text.configure(yscrollcommand=N.set);O=M.join(E.exit_commands);E.commands_text.insert(I,O);E.commands_text.pack(side=L,fill=c,expand=H);N.pack(side='right',fill='y');P=A.Label(F,text='По умолчанию: выход, стоп, завершить, exit, stop, quit, пока',font=(C,8),fg='blue');P.pack(pady=5);G=A.Frame(F);G.pack(pady=10)
		def Q():
			D=E.commands_text.get(I,A.END).strip();C=[A.strip()for A in D.split(M)if A.strip()]
			if not C:K.showwarning(A3,'Должна быть хотя бы одна команда!');return
			E.exit_commands=C;E.log_message(f"Обновлены голосовые команды выхода: {", ".join(C)}",B);E.save_settings();F.destroy()
		def R():B=[s,t,u,v,w,x,y];E.commands_text.delete(I,A.END);E.commands_text.insert(I,M.join(B))
		A.Button(G,text=A1,command=Q,bg='lightgreen',font=(C,10)).pack(side=L,padx=5);A.Button(G,text='Сброс',command=R,bg='orange',font=(C,10)).pack(side=L,padx=5);A.Button(G,text='Отмена',command=F.destroy,bg='lightcoral',font=(C,10)).pack(side=L,padx=5)
	def show_all_devices(D):
		C='end'
		if not D.audio:K.showwarning(A3,'Аудио система не инициализирована');return
		E=A.Toplevel(D.root);E.title('Все аудио устройства');E.geometry('500x400');E.transient(D.root);B=A.Text(E,wrap='word',font=('Consolas',9));J=A.Scrollbar(E,orient=A2,command=B.yview);B.configure(yscrollcommand=J.set)
		try:
			M=D.audio.get_device_count();B.insert(C,f"Найдено {M} аудио устройств:\n\n")
			for F in m(M):
				try:I=D.audio.get_device_info_by_index(F);B.insert(C,f"Устройство {F}:\n");B.insert(C,f"  Название: {I.get(S,"Неизвестно")}\n");B.insert(C,f"  Входы: {I.get(A4,0)}\n");B.insert(C,f"  Выходы: {I.get(A5,0)}\n\n")
				except:B.insert(C,f"Устройство {F}: Ошибка получения информации\n\n")
		except G as N:B.insert(C,f"Ошибка получения списка устройств: {N}")
		B.pack(side=L,fill=c,expand=H,padx=5,pady=5);J.pack(side='right',fill='y')
	def show_about(A):K.showinfo(A0,'Голосовой Эхо-Ассистент v2.0\n\nПростой помощник для Windows 11\nСлушает вашу речь и повторяет её.\n\nИспользует:\n• Vosk для распознавания речи\n• pyttsx3 для синтеза речи\n• PyAudio для работы со звуком')
	def log_message(B,message,category=E,is_exit_command=D,is_ready_message=D):
		C=message
		if not B.log_options.get(category,A.BooleanVar(value=H)).get():return
		if is_exit_command and not B.log_options[X].get():return
		if is_ready_message and not B.log_options[Y].get():return
		if B.log_options[W].get():D=P.strftime('%H:%M:%S');F=f"[{D}] {C}\n";E=f"[{D}] {C}"
		else:F=f"{C}\n";E=C
		print(E)
	def load_settings(A):
		try:
			if os.path.exists(A.settings_file):
				with open(A.settings_file,'r',encoding='utf-8')as F:C=O.load(F)
				if d in C:A.tts_rate.set(C[d])
				if e in C:A.exit_commands=C[e]
				if f in C:
					for(D,H)in C[f].items():
						if D in A.log_options:A.log_options[D].set(H)
				if g in C:A.selected_input.set(C[g])
				if h in C:A.selected_output.set(C[h])
				A.log_message('Настройки загружены из settings.json',B)
		except G as I:A.log_message(f"Ошибка загрузки настроек: {I}",E)
	def save_settings(A):
		try:
			C={d:A.tts_rate.get(),e:A.exit_commands,f:{A:B.get()for(A,B)in A.log_options.items()},g:A.selected_input.get(),h:A.selected_output.get()}
			with open(A.settings_file,Z,encoding='utf-8')as F:O.dump(C,F,ensure_ascii=D,indent=4)
			A.log_message('Настройки сохранены в settings.json',B)
		except G as H:A.log_message(f"Ошибка сохранения настроек: {H}",E)
	def init_audio_system(A):
		P='Unknown'
		try:
			A.log_message('Инициализация аудио системы...',B);A.audio=j.PyAudio();C=A6
			if not os.path.exists(C):raise G(f"Модель Vosk не найдена в {C}")
			A.log_message(f"Загрузка модели Vosk из {C}...",B);A.vosk_model=l.Model(C);A.vosk_rec=l.KaldiRecognizer(A.vosk_model,16000);A.log_message('Инициализация TTS системы...',B);A.tts_engine=k.init();H=A.tts_engine.getProperty(A7)or[];I=F;A.log_message('Поиск русского голоса...',B)
			try:J=list(H)if H else[]
			except(n,o):J=[]
			for L in J:
				D=U(L,S,P);M=U(L,'id',P)
				if A8 in D.lower()or'ru'in M.lower():A.tts_engine.setProperty('voice',M);I=D;A.log_message(f"Выбран русский голос: {D}",B);break
			if not I:A.log_message('Русский голос не найден, используется голос по умолчанию',B)
			N=A.tts_rate.get();A.tts_engine.setProperty(R,N);A.tts_engine.setProperty(i,.9);A.log_message(f"Параметры TTS: скорость={N}, громкость=90%",B);A.refresh_devices();A.log_message('Аудио система инициализирована успешно!',B)
		except G as Q:O=f"Ошибка инициализации: {Q}";A.log_message(O,E);K.showerror(A9,O)
	def refresh_devices(A):
		X='values'
		if not A.audio:return
		try:
			A.log_message('Обновление списка аудио устройств...',B);A.input_devices=[];A.output_devices=[];Y=A.audio.get_device_count();O={};P={}
			for D in m(Y):
				try:
					R=A.audio.get_device_info_by_index(D);T=R.get(S,f"Device {D}");U=R.get(A4,0);W=R.get(A5,0)
					if p(U,(int,q))and U>0:
						J=str(T);Z=['Microphone (Realtek(R) Audio)','РњРёРєСЂРѕС„РѕРЅ (WO Mic Device)','Microphone (3- Mic Device)']
						if V(A in J for A in Z):
							if J not in O:O[J]=D
					if p(W,(int,q))and W>0:
						J=str(T);a=['Первичный звуковой драйвер','Переназначение звуковых устр. - Output'];b=V(A in J for A in a)
						if not b and J not in P:P[J]=D
				except G:continue
			A.input_devices=[(B,A)for(A,B)in O.items()];A.output_devices=[(B,A)for(A,B)in P.items()];H=[A for(B,A)in A.input_devices];I=[A for(B,A)in A.output_devices];A.input_combo[X]=H;A.output_combo[X]=I;M=A.selected_input.get();N=A.selected_output.get();K=F;L=F
			if M and M in H:A.selected_input.set(M);A.log_message(f"Восстановлен микрофон из настроек: {M}",B)
			else:
				for C in H:
					if'WO Mic Device'in C:K=C;break
				if not K and H:K=H[0]
				if K:A.selected_input.set(K);A.log_message(f"Автовыбор микрофона: {K}",B)
			if N and N in I:A.selected_output.set(N);A.log_message(f"Восстановлены динамики из настроек: {N}",B)
			else:
				for C in I:
					if'Speakers (Realtek(R) Audio)'in C:L=C;break
				if not L and I:L=I[0]
				if L:A.selected_output.set(L);A.log_message(f"Автовыбор динамиков: {L}",B)
			A.log_message(f"Найдено {Q(H)} микрофонов и {Q(I)} динамиков",B)
			if A.log_options[B].get():
				if H:
					A.log_message('Доступные микрофоны:',B)
					for(D,C)in r(H):A.log_message(f"  {D+1}. {C}",B)
				if I:
					A.log_message('Доступные динамики:',B)
					for(D,C)in r(I):A.log_message(f"  {D+1}. {C}",B)
		except G as c:A.log_message(f"Ошибка получения устройств: {c}",E)
	def get_device_index(C,device_name,device_list):
		for(A,B)in device_list:
			if B==device_name:return A
	def start_listening(A):
		B='Внимание'
		if A.is_listening:return
		if not A.selected_input.get():K.showwarning(B,'Выберите устройство ввода!');return
		if not A.selected_output.get():K.showwarning(B,'Выберите устройство вывода!');return
		A.is_listening=H;A.start_btn.config(state=b);A.stop_btn.config(state=AA);A.update_window_title('Слушаю...');A.listen_thread=T.Thread(target=A.listen_loop,daemon=H);A.listen_thread.start();C=A.selected_input.get();D=A.selected_output.get();A.log_message(f"Начато прослушивание с устройствами:",I);A.log_message(f"  Микрофон: {C}",I);A.log_message(f"  Динамики: {D}",I)
	def stop_listening(A):A.is_listening=D;A.start_btn.config(state=AA);A.stop_btn.config(state=b);A.update_window_title('Остановлено');A.log_message('Прослушивание остановлено',I)
	def listen_loop(A):
		try:
			L=A.get_device_index(A.selected_input.get(),A.input_devices)
			if L is F:A.log_message('Ошибка: не удалось найти устройство ввода',E);return
			M=4096;R=16000
			if A.audio is F:A.log_message('Ошибка: аудио система не инициализирована',E);return
			C=A.audio.open(format=j.paInt16,channels=1,rate=R,input=H,input_device_index=L,frames_per_buffer=M);A.log_message(f"Подключен микрофон: {A.selected_input.get()}",I);A.log_message(f"Готов к распознаванию речи (16kHz, 1 канал)",I);A.log_message('Говорите что-нибудь...',I)
			while A.is_listening:
				try:
					S=C.read(M,exception_on_overflow=D)
					if A.vosk_rec is not F and A.vosk_rec.AcceptWaveform(S):
						U=O.loads(A.vosk_rec.Result());B=U.get('text','').strip()
						if B:
							A.log_message(f"Распознана фраза: '{B}' (длина: {Q(B)} символов)",N)
							if V(A in B.lower()for A in A.exit_commands):A.log_message(f"Команда выхода распознана в: '{B}'",N,is_exit_command=H);W='До свидания! Завершаю работу.';A.speak_text(W);T.Timer(3.,A.stop_listening).start();return
							A.speak_text(B)
						else:
							J=A.vosk_rec.PartialResult()if A.vosk_rec else'{}'
							if'"partial"'in J and Q(J)>20:
								X=O.loads(J);P=X.get('partial','')
								if P.strip():A.log_message(f"Частичное распознавание: '{P}'",E)
				except G as K:
					if A.is_listening:A.log_message(f"Ошибка обработки аудио: {K}",E)
			C.stop_stream();C.close()
		except G as K:A.log_message(f"Ошибка в цикле прослушивания: {K}",E);A.stop_listening()
	def speak_text(A,text):
		C=text
		if not C.strip():return
		A.speech_counter+=1;B=A.speech_counter
		def I():
			try:
				L=0
				while A.tts_busy and L<30:P.sleep(.1);L+=1
				if A.tts_busy:A.log_message(f"TTS заблокирована, принудительный сброс для #{B}",E);A.tts_busy=D
				A.tts_busy=H;A.log_message(f"СТАРТ произношения #{B}: '{C}'",J)
				if A.tts_engine is not F:
					if B>1:
						try:
							A.log_message(f"ПОЛНАЯ переинициализация TTS для #{B}",J)
							try:A.tts_engine.stop();del A.tts_engine
							except:pass
							A.tts_engine=k.init();M=A.tts_engine.getProperty(A7)or[]
							try:O=list(M)if M else[]
							except(n,o):O=[]
							for Q in O:
								if A8 in U(Q,S,'').lower():A.tts_engine.setProperty('voice',Q.id);break
							I=A.tts_rate.get();A.tts_engine.setProperty(R,I);A.tts_engine.setProperty(i,1.);A.log_message(f"TTS переинициализирован для #{B}",J)
						except G as K:A.log_message(f"Ошибка переинициализации TTS: {K}",E)
					else:
						try:A.tts_engine.stop();I=A.tts_rate.get();A.tts_engine.setProperty(R,I);A.tts_engine.setProperty(i,1.)
						except:pass
					T=P.time();A.log_message(f"Отправляю в TTS #{B}: '{C}'",J);A.tts_engine.say(C);A.log_message(f"Ожидание воспроизведения #{B}...",J);A.tts_engine.runAndWait();V=P.time();W=round(V-T,2);A.log_message(f"ГОТОВО #{B} за {W}с: '{C}'",N,is_ready_message=H)
				else:A.log_message('TTS система недоступна',E)
			except G as K:A.log_message(f"КРИТИЧЕСКАЯ ошибка #{B}: {K}",E)
			finally:A.tts_busy=D;A.log_message(f"TTS освобожден #{B}",J)
		K=T.Thread(target=I,daemon=H);K.start()
	def on_closing(A):
		A.stop_listening();A.save_settings()
		if A.audio:A.audio.terminate()
		if A.tts_engine:
			try:A.tts_engine.stop()
			except:pass
		A.root.destroy()
def AC():
	C=A6
	if not os.path.exists(C):K.showerror(A9,f"Модель Vosk не найдена в {C}\n\nСкачайте русскую модель с https://alphacephei.com/vosk/models\nи распакуйте в папку C:\\vosk");return 1
	B=A.Tk();D=AB(B);B.protocol('WM_DELETE_WINDOW',D.on_closing);B.mainloop();return 0
if __name__=='__main__':sys.exit(AC())