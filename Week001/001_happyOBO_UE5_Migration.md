## 1주차 스터디 내용


### 1. UE4 UE5 변경 내용 분석

- 해당 링크에 정리
    - [https://github.com/happyOBO/Unreal_Study/blob/main/UE5/UE4vsUE5.md](https://github.com/happyOBO/Unreal_Study/blob/main/UE5/UE4vsUE5.md)


### 2. UE4 프로젝트 마이그래이션

- 1번 내용을 확인해보면서, UE4 프로젝트를 바로 UE5로 옮길 수 있다는 것을 알게 되었다.
    - [마이그레이션 참고 링크](https://docs.unrealengine.com/5.0/en-US/unreal-engine-5-migration-guide/)

- 그래서 해당 프로젝트를 참고 링크를 토대로 바로 마이그레이션을 진행하고, 추가 기능을 UE5 기반으로 제작하는 것으로 변경한다.

- 다만, 두가지 문제 상황 발생
    1. UE5 로 C++ 빌드시 `CreateWidget` 에서 빌드 오류
    2. 마우스 클릭 시 블럭이 깨지는 기능이 사라짐.


#### 1. UE5 로 C++ 빌드시 `CreateWidget` 에서 빌드 오류

- 원래 아래 함수가 템플릿에서 옵셔널하게 타입을 지정하고 있어서 `UUserWidget` 만 타입 지정을 해놓고 작성을했는데, 인수 목록이 일치하는 함수 템플릿 인스턴스가 없다는 오류가 나오고 있음.


```cpp
CurrentWidget = CreateWidget<UUserWidget>(PlayerOwner, WidgetToApply); // 원래 코드.

// UserWidget 에서 정의되어있는 CreateWidget 함수
template <typename WidgetT = UUserWidget, typename OwnerT = UObject>
WidgetT* CreateWidget(OwnerT* OwningObject, TSubclassOf<UUserWidget> UserWidgetClass = WidgetT::StaticClass(), FName WidgetName = NAME_None)
{
	static_assert(TIsDerivedFrom<WidgetT, UUserWidget>::IsDerived, "CreateWidget can only be used to create UserWidget instances. If creating a UWidget, use WidgetTree::ConstructWidget.");
	
	static_assert(TIsDerivedFrom<OwnerT, UWidget>::IsDerived
		|| TIsDerivedFrom<OwnerT, UWidgetTree>::IsDerived
		|| TIsDerivedFrom<OwnerT, APlayerController>::IsDerived
		|| TIsDerivedFrom<OwnerT, UGameInstance>::IsDerived
		|| TIsDerivedFrom<OwnerT, UWorld>::IsDerived, "The given OwningObject is not of a supported type for use with CreateWidget.");

	SCOPE_CYCLE_COUNTER(STAT_CreateWidget);

	if (OwningObject)
	{
		return Cast<WidgetT>(UUserWidget::CreateWidgetInstance(*OwningObject, UserWidgetClass, WidgetName));
	}
	return nullptr;
}
```

- `OwnerT` 가 `UObject` 로 되어있으나, `PlayerOwner` 는 `APlayerController` 타입이므로 아래와 같이 타입을 지정해주니 빌드 성공 되었다.
    - [커밋 링크](https://github.com/happyOBO/MinecraftUE5/commit/8c233dca8727e6b554172f78c51e87064641d153)