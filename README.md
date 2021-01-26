# Engnharia de Sistemas Técnicas de Modelagem de Sistemas
Repositório compartilhado para tradução de scripts matlab para python no intento de manter mais acessível aos alunos do curso de engenharia de sistemas da UFMG

## Docker 
Para agilizar o tempo de desenvolvimento é possível instalar o Docker em Windows, MacOs e distribuíções Linux.
Assumindo que o aluno tenha acesso ao sistema Linux, pode se fazer a instalação do docker utilizando o script abaixo:
```shell
# Download e instalação oficial do docker 
# alteração do usuário atual para utilizar docker sem elevar permissões
curl -fsSL https://get.docker.com | sudo sh - && sudo usermod -aG docker $USER
```
Após a instalação confira se ocorreu tudo certo (pode ser necessário efetuar *logoff* e *login*)
`docker info` esse comando não deve retornar erro de qualquer tipo.

## Utilização do Jupyter em container
```shell
docker run --rm \
-p 8888:8888 \
-e JUPYTER_ENABLE_LAB=yes \
-v "$PWD":/home/jovyan/work \
-w /home/jovyan/work  \
jupyter/datascience-notebook
```
Execute esse comando na mesma pasta de seu projeto. Caso contrário o docker não fará mágica,
o parâmetro  `-v` está fazendo o mapeamento da pasta onde esta executando o comando para o docker 
(para ficar simples essa explicação serve)

Logo appós executar o docker com sucesso deve aparecer uma URL para entrar no servidor do jupyter:
```shell
> Executing the command: jupyter lab
[I 23:20:20.627 LabApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 23:20:21.967 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.8/site-packages/jupyterlab
[I 23:20:21.967 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 23:20:21.976 LabApp] Serving notebooks from local directory: /home/jovyan/work
[I 23:20:21.976 LabApp] Jupyter Notebook 6.1.4 is running at:
[I 23:20:21.976 LabApp] http://17b1ebee0135:8888/?token=9db18826e53585b64c6384c041ea94e2cd79d0a0707b6e96
[I 23:20:21.976 LabApp]  or http://127.0.0.1:8888/?token=9db18826e53585b64c6384c041ea94e2cd79d0a0707b6e96
[I 23:20:21.976 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 23:20:21.989 LabApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://17b1ebee0135:8888/?token=9db18826e53585b64c6384c041ea94e2cd79d0a0707b6e96
     or http://127.0.0.1:8888/?token=9db18826e53585b64c6384c041ea94e2cd79d0a0707b6e96
```
Não utilize esse comando em ambiente de produção na sua empresa. Haverá problemas.



