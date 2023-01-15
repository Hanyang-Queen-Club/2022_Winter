### 마인크래프트 리팩토링

- 생성 가능한 도구를 계산하는 함수를 원래는 틱 마다 호출하는 방식
- 이것을 생성 상자 --> 인벤토리 또는 인벤토리 --> 생성 상자로 이동할 때 해당 함수를 호출하게끔 했다. 
- [참고링크](https://github.com/happyOBO/MinecraftUE5/commit/06054d0ab5cad3edfb58076f0f805d453a91bcd2)