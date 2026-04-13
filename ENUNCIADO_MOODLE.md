# Trabalho Prático — Testes de Componente com `pytest`
## Tema: Sistema de Hotelaria

## Objetivo
Você recebeu um pequeno sistema de hotelaria já implementado. O projeto contém:

- código-fonte do subsistema;
- testes de unidade prontos;
- estrutura básica de pastas.

Seu trabalho é **criar os testes de componente** para esse subsistema, utilizando `pytest`.

Os testes de componente devem verificar a colaboração real entre as classes do módulo, cobrindo fluxos de negócio relevantes. Não é permitido substituir as classes internas do subsistema por mocks. Como este trabalho foca em teste de componente, ele **não exige banco de dados real, rede ou Docker**.

## Estrutura do sistema
O sistema possui as seguintes classes:

- `RoomRepository`
- `GuestRepository`
- `StayRepository`
- `WaitlistRepository`
- `HotelService`

## Regras de negócio

### Check-in
Um hóspede pode fazer check-in em um quarto somente se:

- o hóspede existir;
- o quarto existir;
- o hóspede não estiver bloqueado;
- o hóspede não tiver débito pendente;
- o quarto estiver disponível;
- o hóspede tiver menos de 2 hospedagens ativas;
- o quarto não estiver em fila de espera para outro hóspede.

Quando o check-in é realizado com sucesso:

- o quarto deixa de estar disponível;
- a hospedagem é registrada;
- se havia fila de espera do mesmo hóspede para esse quarto, ela deve ser removida.

### Check-out
Ao realizar check-out:

- a hospedagem ativa correspondente deve existir;
- a hospedagem é encerrada;
- se não houver fila de espera para o quarto, ele volta a ficar disponível;
- se houver fila de espera, o quarto continua indisponível, aguardando o próximo hóspede da fila.

### Fila de espera
Um hóspede pode entrar na fila de espera de um quarto somente se:

- o hóspede existir;
- o quarto existir;
- o hóspede não estiver bloqueado;
- o hóspede não tiver débito pendente;
- o quarto estiver indisponível;
- o hóspede não tiver uma entrada duplicada na fila para o mesmo quarto;
- o hóspede não for quem já está hospedado naquele quarto.

A fila deve respeitar a ordem de chegada.

## O que deve ser implementado
Você deve criar os testes de componente em:

```text
tests/components/
```

Sugestão de arquivo:

```text
tests/components/test_hotel_component.py
```

## Cenários obrigatórios
Implemente testes de componente cobrindo, no mínimo, os seguintes cenários:

1. check-in com sucesso;
2. check-in de quarto inexistente;
3. check-in por hóspede inexistente;
4. check-in bloqueado por débito pendente;
5. check-in bloqueado por hóspede bloqueado;
6. check-in bloqueado por limite de 2 hospedagens ativas;
7. entrada em fila de espera com sucesso para quarto indisponível;
8. tentativa de entrada duplicada na fila de espera;
9. check-out simples sem fila de espera;
10. check-out com fila de espera, mantendo o quarto indisponível;
11. check-in bem-sucedido por hóspede que estava na fila do mesmo quarto, removendo a fila;
12. sequência completa: check-in → fila de espera por outro hóspede → check-out → tentativa de novo check-in.

## Requisitos
Os testes devem:

- usar as classes reais do subsistema;
- refletir fluxos de negócio;
- ser determinísticos;
- ter nomes descritivos;
- evitar duplicação excessiva;
- usar `pytest`.

## O que já está pronto
Os testes de unidade em `tests/unit/` já foram fornecidos. Você **não deve reescrevê-los**.

## Execução
Para rodar os testes de unidade:

```bash
pytest tests/unit
```

Para rodar todos os testes:

```bash
pytest
```
