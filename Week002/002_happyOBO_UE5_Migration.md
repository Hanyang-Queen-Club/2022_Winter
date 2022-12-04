## 2주차 스터디 내용

### 오류 내용 변경

- 마우스 클릭 시 블럭이 깨지는 기능이 동작하지 않았던 이유는 마이그레이션 때문이 아니라, 
- 멀티 플레이어 구조로 바꾸면서, Standalone 플랫폼에서 제대로 동작하지 않게되었던, 기존 버그로 인해 발생한 문제였음.
- 그래서 클라이언트로 실행하면, 블럭 깨는 기능이 잘 돌아가고 있음.
- Stanalone 에서도 동일 동작하게끔 코드 수정 필요.

### 해결 방법

- 커밋 로그
	- [8c233dc](https://github.com/happyOBO/MinecraftUE5/commit/ac4cddbebef0069ee6c896fc83d9af631e59a74a)
	- [ac4cddb](https://github.com/happyOBO/MinecraftUE5/commit/b586a5e5be8be25e5169d61c838125f45850b215)

- 아래처럼 Role 값이 `ROLE_Authority` 가 아닐때, 서버 RPC 함수를 호출하게끔 되어있는 경우가 많은데,, 요렇게 하면 Standalone 은 `ROLE_Authority` 이므로 해당 함수를 호출할 수 없으므로 `GetNetMode()` 값으로 조건문을 변경했다. 

```cpp
void AMinecraftUECharacter::CheckForBlocks()
{
	if (GetLocalRole() < ROLE_Authority) // if (GetNetMode() != NM_DedicatedServer)
	{
		FHitResult LinetraceHit;
```

- 요렇게 해서 블럭이 깨지는건 Standalone 에서도 나오게끔 했지만, 깨지는 매테리얼 적용이 안되었다.
- 그 이유는 블럭이 깨지는 정도를 `BreakingStage` 를 통해 계산을 하고, 이를 리플리케이션 함수 `OnRep_Breaking` 를 통해서 하고 있는데, 이게 Stanalone 에서는 안불리므로, 해당 변수를 계산하는 함수에서 별도로 `OnRep_Breaking` 함수를 호출해주도록 처리한다.

```cpp
++BreakingStage; // 블럭 깨지는 정도 값 증가
if (GetNetMode() == NM_Standalone)
{
	OnRep_Breaking();
}
```