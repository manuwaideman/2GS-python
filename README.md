# Triagem de Saúde Mental

## Problema
O aumento alarmante de 25% na prevalência global de ansiedade e depressão, destacado pela Organização Mundial da Saúde (OMS), revela uma crise de saúde mental. Interrupções nos serviços deixaram lacunas no atendimento, exacerbando a escassez crônica de recursos. A busca online por suporte destaca a necessidade urgente de ferramentas digitais acessíveis. Um estudo da Secretaria de Atenção Primária aponta que a detecção precoce de sinais de transtornos mentais é crucial para prevenir, promover e tratar problemas de saúde mental. Ressalta também a importância de ações preventivas e intervencionistas para melhorar o bem-estar. De acordo com Natália Silva, psicóloga, a escassez global de recursos de saúde mental contrasta com a importância equiparada à alimentação, educação e emprego. A falta de acesso ao cuidado agravada por desafios econômicos ressalta a necessidade crítica de soluções inovadoras e acessíveis, como nosso projeto, que surge como uma proposta para realizar triagens de saúde mental de forma eficiente, proporcionando suporte emocional personalizado.

## Código em Python - Triagem de Saúde Mental

O código em Python apresenta uma aplicação de triagem de saúde mental, interativa e acessível. Os usuários respondem a perguntas sobre tristeza, sono, ansiedade e apetite, com respostas registradas em um arquivo JSON. A solução permite realizar triagens, salvar respostas e visualizar registros anteriores.

### Funcionalidades

#### Menu de Opções
O código implementa um menu interativo oferecendo três principais funcionalidades: realizar triagem, visualizar registros e sair do programa. Isso proporciona uma experiência intuitiva e acessível ao usuário.

#### Validações nas Entradas de Dados
A função `validar_entrada` garante que as opções inseridas pelo usuário sejam válidas (no caso, 's', 'n', '1', '2', ou '3'), evitando entradas incorretas.

#### Tratamento de Exceções
O código utiliza blocos `try` e `except` para tratar exceções ao tentar abrir o arquivo de registros ('registros.json'). Isso evita erros caso o arquivo não exista no início da execução.

#### Estruturas de Decisão e Repetição
Estruturas condicionais (`if`, `elif`, `else`) são aplicadas no menu para direcionar o programa de acordo com a escolha do usuário. O loop `while` garante a repetição do menu até que o usuário escolha sair.

#### Funções com Parâmetros e Retorno
As funções `validar_entrada`, `coletar_respostas`, `salvar_respostas`, e `visualizar_registros` são definidas com parâmetros e retornos adequados, promovendo modularidade e reusabilidade do código.

#### Dicionários e Arquivos como Bancos de Dados
O dicionário `perguntas` armazena as perguntas de triagem e suas chaves são utilizadas para identificar as respostas do usuário. O arquivo 'registros.json' é utilizado como banco de dados, armazenando todas as respostas das triagens.

## Diferencial da Solução

### Abordagem Interativa
Nosso projeto utiliza uma abordagem interativa para coletar dados relevantes, envolvendo o usuário no processo de triagem de forma amigável.

### Registro de Histórico
Todas as respostas são registradas em um arquivo JSON, permitindo uma análise histórica das triagens e a identificação de padrões ao longo do tempo.

### Facilidade de Uso
O menu interativo torna a utilização da aplicação simples e acessível, oferecendo opções claras para realizar triagens, visualizar registros ou sair do programa.

## Instruções de Uso

1. Execute o script em Python.
2. Escolha a opção desejada no menu: realizar triagem, visualizar registros ou sair.
3. Durante a triagem, responda às perguntas de acordo com sua experiência.
4. As respostas serão registradas no arquivo 'registros.json'.
5. Ao visualizar registros, o histórico de triagens será exibido, se disponível.

## Próximos Passos e Contribuições

O código atual representa uma versão inicial da solução. Para aprimorar a solução, sugestões incluem:

- Implementação de análise mais avançada dos registros para identificação de padrões.
- Integração de recursos adicionais, como análise de linguagem natural para respostas mais abertas.
- Aprimoramento da interface do usuário para maior usabilidade.

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias ou adicionar novas funcionalidades.

