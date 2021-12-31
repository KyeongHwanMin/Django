# ES6+ 문법 및 리액트 기초 익히기

## nodejs 설치

데스크탑에서 구동할 수 있는 JavaScript Runtime인 Nodejs를 통해, 자바스크립트 문법 익히기

nodejs LTS(Long Term Support)버전 설치

방법1) 공식사이트에서 다운받아 설치 : https://nodejs.org
방법2) 팩키지 관리자 chocolatey를 통한 설치 -> 쉘> choco install nodejs-lts
방법3) Docker를 활용한 개발환경



### 팩키지 관리자
#### npm (node package manager) : nodejs 기본 팩키지 관리자

npm install --global 팩키지명
npm install 팩키지명



#### yarn : 페이스북 주도로 개발된 팩키지 관리자

설치> npm install --global yarn
yarn global add 팩키지명
yarn add 팩키지명
yarn add --dev 팩키지명
yarn add



#### Visual Studio Code 추천 확장
Korean Language Pack for Visual Studio Code : UI를 한국어로 변경
Active File in StatusBar : 최하단 바에 작업 중인 파일 경로 노출
Auto Rename Tag : 짝이 되는 태그도 동시에 수정
Color Highlight : 컬러코드 텍스트의 배경색을 해당 색상으로 보여줌
debugger-for-chome : 크롬 개발자 도구에서 디버깅하던 것을 VSCode에서 가능
DotENV : .env 파일에 대한 문법 강조
ESLint : JavaScript 코드 정적 분석 à "eslint.autoFixOnSave": true 설정 추천
Prettier : code formatter à "editor.formatOnSave": true 설정 추천
TODO Highlight : TODO highlight



#### 꼭 알아야할 문법들
상수/변수 선언 (const/let)
Object 선언, 단축 속성, key 계산, 객체 복사
Template Literals
배열/객체 비구조화 (Array/Object Destructuring)
전개 연산자 (Spread Operator)
함수와 인자 (Functions, Parameters, Named Parameters)
Arrow Functions
Promise와 async/await
클래스와 상속
모듈 시스템
고차 함수 (High Order Function)



#### 상수/변수 선언
var 대신에 const(상수) 혹은 let(변수)을 사용 -> block scope
• const : 재할당 불가. 내부 속성값은 수정 가능.
• let : Lexical Variable Scoping을 지원하는 변수 선언 문법

const tom = {lang: "Python"};

tom.lang = "JavaScript";



var div;
var container = document.getElementsByTagName('body')[0];
for(let i=0; i<5; i++) {
	div = document.createElement('div’);
	div.onclick = function() {
	alert("clicked : #" + i);
	};
	div.innerHTML = "#" + i;
	container.appendChild(div);
}



### 모듈 시스템
예전 웹 상의 자바스크립트에서는 script 태그를 통해서만이 로딩
모두 전역 객체에 바인딩

2가지 모듈 시스템
CommonJS Module : nodejs에서 주로 활용
ES6 Module : 리액트에서 주로 활용



### 모듈 / ES6 module
React를 쓰실 때, 사용할 모듈 시스템
IE를 포함한 구형 브라우저에서는 미지원
node 이후에 ES6 Module이 나왔기에, node에서는 왠만한 ES6 문법은
지원하지만, 모듈은 ES6 module을 지원하지 않고, CommonJS만을 지원
문법 : export, export default, import ... from



### 고차 함수 (High Order Function)
함수를 인자로 받거나 반환이 가능하고, 다른 함수를 조작하는 함수
함수/클래스 역시 모두 객체



## 순수 함수와 커링 기법



### 리액트는 함수형 프로그래밍을 적극 활용
**컴포넌트의 많은 루틴을 순수 함수로서 작성하기를 요구**
	상탯값/속성값이 같으면, 항상 같은 값을 반환해야합니다.
	다른 Side effects를 발생시키지 않아야 합니다. (HTTP 요청, 데이터 저장, 쿠키 조작 등)
**컴포넌트의 상탯값은 불변 객체 (Immutable Object)로 관리해야만 합니다.**
	수정할 때에는 기존 값을 변경하는 것이 아니라, 같은 이름의 새로운 객체를 생성합니다.
**이를 통해, UI개발의 복잡도를 낮추고, 버그 발생 확률도 줄입니다.**
const Header = (props) => (

​	<div>

​		<h1>{props.title}</h1>

​	</div>

)

### 순수 함수
하나 이상의 인자를 받고, 인자를 변경하지 않고, 참조하여 새로운 값을 반환
Side Effects가 없도록 구성

### 순수 함수를 활용한 데이터 변환
reduce, filter, map, join 등

### 커링 (Currying)
일부의 인자를 고정한 새로운 함수를 반환하는 함수를 만드는 기법