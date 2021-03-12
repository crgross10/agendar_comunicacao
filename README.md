# agendar_comunicacao
 app teste para agendar envio de comunicação
 
Como rodar o projeto?
Clone esse repositório.
-- git clone https://github.com/crgross10/agendar_comunicacao.git
Crie um virtualenv com Python 3. 
-- pip3 install virtualenvwrapper  (OBS: WINDOWS 10 ---> virtualenvwrapper-win )
-- mkvirtualenv <nome_para_virtual_env>
Ative o virtualenv.
-- workorn  <nome_da_virtual_env_criada_passo_anterior>
Instale as dependências.
--pip install -r requirements.txt
Rode as migrações.
--python manage.py makemigrations
--python manage.py migrate

