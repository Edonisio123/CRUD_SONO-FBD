# CRUD_SONO-FBD
CRUD de controle de sono. Desenvolvido com Python, Panel e PostgreSQL

🎯 Objetivo do Projeto
Criar um sistema simples e visual para registrar e gerenciar hábitos de sono dos usuários, utilizando uma interface web interativa conectada a um banco de dados PostgreSQL.

⚙️ Tecnologias Utilizadas
Python

Panel (interface gráfica web)

PostgreSQL (armazenamento dos dados)

Pandas e SQLAlchemy (manipulação e consulta dos dados)

dotenv (para segurança nas credenciais)

🛠️ Estrutura da Tabela sono
Campo	                Tipo	                        Descrição
id	                  SERIAL	                      Identificador do registro (PK)
usuario_id	          INT	ID                        do usuário responsável
data	                DATE	                        Data do registro
hora_dormir	          TIME	                        Horário em que dormiu
hora_acordar	        TIME	                        Horário em que acordou
nota_qualidade	      INT (0 a 10)	                Qualidade percebida do sono

🧩 Funcionalidades do Sistema
🔍 Consultar registros
Permite visualizar todos os registros do banco.

Pode filtrar por ID do usuário.

➕ Inserir novo registro
Preenche os campos no formulário.

Clica no botão Inserir.

O dado é salvo automaticamente no banco.

🔄 Atualizar registro
Preenche o campo ID do Registro que será alterado.

Atualiza os dados no formulário.

Clica no botão Atualizar.

❌ Excluir registro
Informa o ID do Registro.

Clica no botão Excluir para removê-lo do banco.

🧪 Fluxo de Funcionamento
O usuário abre a interface no navegador.

Preenche os campos ou seleciona ações.

O Panel envia comandos SQL ao PostgreSQL.

O banco responde com sucesso ou erro, e a interface atualiza.

💡 Vantagens do Projeto
Interface intuitiva (não precisa saber SQL)

Armazenamento seguro e estruturado dos dados

Fácil expansão (outros hábitos, exportar CSV etc.)

Pode ser usado por nutricionistas, médicos ou pessoas que monitoram sua rotina de sono

📌 Possíveis Melhorias Futuras
Login de usuários

Gráficos com análise de sono

Exportação de relatórios

Integração com notificações ou sensores (IoT)

