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



## babel,webpack,create-react-app

babel과 webpack 그리고 create-react-appbabel-preset-env
• 디폴트로 동작으로 ES6 이상의 preset을 적용하여, ES5로 transpiling
• 개별 지정보다 본 preset을 권장
• https://babeljs.io/env



### webpack (module bundler)
javascript, jsx, css, sass, less, es6, 이미지, HTML, 폰트 등 거의 모든 것이
모듈이 될 수 있으며, 하나의 파일 (bundle)로 묶을 수 있다.
모듈성과 네트워크 성능 향상
Features
• 코드를 필요할 때, 로딩 가능
• Minifying : 불필요한 코드, 공백/줄바꿈, 긴 이름 등을 줄여, 파일 크기 줄이기
• HMR (Hot module replacement) : 개발모드에서 원본 소스코드 변경을 감지하여, 변경된 모듈만 즉시 갱신
지원 Loaders
• babel-loader : ES6나 리액트 코드를 transpiling
• css-loader : 설정에 따라 postcss-loader, sass-loader를 추가로 설정. css를 HTML내에서 <link /> 엘리먼트로
포함시킬 필요없이 JS/JSX단에서 임포트하여 React 컴포넌트에 즉시 적용 가능



### create-react-app
webpack, babel, eslilnt 등의 기본 설정이 된 리액트 프로젝트 생성

설치> yarn global add create-react-app
프로젝트 생성
쉘> create-react-app --help
쉘> create-react-app <프로젝트-디렉토리>

**개발서버 구동**
쉘> cd <디렉토리>
쉘> yarn start



## CRA 프로젝트에 Ant Design 적용하기

Ant Design
알리바바 그룹에서 개발한 UI 프레임워크
	React, Vue, Angular 등을 지원
깊은 디자인 철학을 가진 UX
	Button, Grid, Layout, Form 등의 컴포넌트를 지원



### CRA 프로젝트에 적용하기
1. yarn add antd
2. App.js 참조 경로에 antd/dist/antd.css 추가하기



## React Element

### 리액트
**UI 라이브러리 (웹 프론트엔드 및 앱 Native, VR 등에서 활용)**
**UI데이터를 관리하는 방법을 제공**
	부모 컴포넌트로부터 내려받는 속성값 à props
	컴포넌트 내부에서 생성/관리되는 상탯값 à state
**UI데이터(UI에 연결된 속성값/상탯값)가 변경되면, 해당 컴포넌트의 render()**
**함수가 호출이 되어 화면을 자동으로 갱신**
	클래스형 컴포넌트에서는 render() 함수가 호출
	함수형 컴포넌트에서는 그 함수가 매번 호출. 컴포넌트에서 유지해야할 값들은 Hook을 통해 관리

## 리액트의 핵심 – 선언적 UI (Declarative UI)
**UI에 변화를 가할 때마다 일일이 코드를 수행하는 것이 아니라,**
	데이터 (속성값/상탯값)에 맞춰 보여질 UI를 미리 선언해두면,
	데이터 변경가 변경되면, 그 즉시 데이터에 맞춰 UI가 그려진다.



### React Element
**화면을 담당하며, React 앱의 가장 작은 단위**

// jsx 문법

const reactElement1 = <h1>Hello. React!</h1>

// js 문법

const reactElement2 = React.createElement('h1', null, 'Hello, React!');

**일반 객체 (Plain Object)**
**React DOM은 React Element와 일치하도록 DOM을 업데이트**
**Element는 Component에서 화면을 담당**
	컴포넌트의 주요 구성요소 : 속성값 (props), 상탯값 (state), 엘리먼트 (element), 그리고 로직



### React Component
**Component를 통해 UI를 재사용 가능한 개별적인 여러 조각으로 나눕니다.**
	개념적으로 JavaScript 함수와 유사
	속성값을 전달받아, Element를 반환
**클래스로 구현하는 컴포넌트가 먼저 지원되었으며, 최근에 함수로 구현하는 컴포넌트를 지원**



### React.createElement
React.createElement(component, props, ...children) è ReactElement
1. component
• 문자열이나 리액트 컴포넌트. 문자열일 경우 DOM 요소를 생성
2. props
• 컴포넌트가 사용하는 데이터
3. ...children
• 해당 컴포넌트가 감싸고 있는 내부의 컴포넌트들을 다수 지정



## ES6+ 문법 및 리액트 기초 익히기

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



## babel,webpack,create-react-app

babel과 webpack 그리고 create-react-appbabel-preset-env
• 디폴트로 동작으로 ES6 이상의 preset을 적용하여, ES5로 transpiling
• 개별 지정보다 본 preset을 권장
• https://babeljs.io/env



### webpack (module bundler)

javascript, jsx, css, sass, less, es6, 이미지, HTML, 폰트 등 거의 모든 것이
모듈이 될 수 있으며, 하나의 파일 (bundle)로 묶을 수 있다.
모듈성과 네트워크 성능 향상
Features
• 코드를 필요할 때, 로딩 가능
• Minifying : 불필요한 코드, 공백/줄바꿈, 긴 이름 등을 줄여, 파일 크기 줄이기
• HMR (Hot module replacement) : 개발모드에서 원본 소스코드 변경을 감지하여, 변경된 모듈만 즉시 갱신
지원 Loaders
• babel-loader : ES6나 리액트 코드를 transpiling
• css-loader : 설정에 따라 postcss-loader, sass-loader를 추가로 설정. css를 HTML내에서 <link /> 엘리먼트로
포함시킬 필요없이 JS/JSX단에서 임포트하여 React 컴포넌트에 즉시 적용 가능



### create-react-app

webpack, babel, eslilnt 등의 기본 설정이 된 리액트 프로젝트 생성

설치> yarn global add create-react-app
프로젝트 생성
쉘> create-react-app --help
쉘> create-react-app <프로젝트-디렉토리>

**개발서버 구동**
쉘> cd <디렉토리>
쉘> yarn start



## CRA 프로젝트에 Ant Design 적용하기

Ant Design
알리바바 그룹에서 개발한 UI 프레임워크
	React, Vue, Angular 등을 지원
깊은 디자인 철학을 가진 UX
	Button, Grid, Layout, Form 등의 컴포넌트를 지원



### CRA 프로젝트에 적용하기

1. yarn add antd
2. App.js 참조 경로에 antd/dist/antd.css 추가하기



## React Element

### 리액트

**UI 라이브러리 (웹 프론트엔드 및 앱 Native, VR 등에서 활용)**
**UI데이터를 관리하는 방법을 제공**
	부모 컴포넌트로부터 내려받는 속성값 à props
	컴포넌트 내부에서 생성/관리되는 상탯값 à state
**UI데이터(UI에 연결된 속성값/상탯값)가 변경되면, 해당 컴포넌트의 render()**
**함수가 호출이 되어 화면을 자동으로 갱신**
	클래스형 컴포넌트에서는 render() 함수가 호출
	함수형 컴포넌트에서는 그 함수가 매번 호출. 컴포넌트에서 유지해야할 값들은 Hook을 통해 관리

## 리액트의 핵심 – 선언적 UI (Declarative UI)

**UI에 변화를 가할 때마다 일일이 코드를 수행하는 것이 아니라,**
	데이터 (속성값/상탯값)에 맞춰 보여질 UI를 미리 선언해두면,
	데이터 변경가 변경되면, 그 즉시 데이터에 맞춰 UI가 그려진다.



### React Element

**화면을 담당하며, React 앱의 가장 작은 단위**

// jsx 문법

const reactElement1 = <h1>Hello. React!</h1>

// js 문법

const reactElement2 = React.createElement('h1', null, 'Hello, React!');

**일반 객체 (Plain Object)**
**React DOM은 React Element와 일치하도록 DOM을 업데이트**
**Element는 Component에서 화면을 담당**
	컴포넌트의 주요 구성요소 : 속성값 (props), 상탯값 (state), 엘리먼트 (element), 그리고 로직



### React Component

**Component를 통해 UI를 재사용 가능한 개별적인 여러 조각으로 나눕니다.**
	개념적으로 JavaScript 함수와 유사
	속성값을 전달받아, Element를 반환
**클래스로 구현하는 컴포넌트가 먼저 지원되었으며, 최근에 함수로 구현하는 컴포넌트를 지원**



### React.createElement

React.createElement(component, props, ...children) è ReactElement

1. component
   • 문자열이나 리액트 컴포넌트. 문자열일 경우 DOM 요소를 생성
2. props
   • 컴포넌트가 사용하는 데이터
3. ...children
   • 해당 컴포넌트가 감싸고 있는 내부의 컴포넌트들을 다수 지정



## 상탯값 (state)

### 상탯값 (state)
UI (엘리먼트)로의 반영을 위해, 유지해야할 값들의 묶음
상탯값은 어디에 저장/관리되나요?
	각 컴포넌트 내에서만 사용되는 값들은 컴포넌트 안에서 생성/갱신 -> 리액트 기본 기본으로 동작
	여러 컴포넌트에서 사용되는 값들은 별도 공간에서 생성/갱신 -> 이때 Redux, Context API, MobX 등을 활용하면 편리
컴포넌트에서 상탯값에 대한 getter/setter 함수를 제공해줍니다.
	상탯값을 직접 변경하진 말아요. -> 성능 하락. 강제 UI 업데이트를 할 순 있지만 ... L



### setState
ReactComponent.setState(
객체 또는 함수,
처리가_끝났을_때_호출되는_콜백_함수
)
비동기로 동작
변경할 특정 state값들이 담긴 object를 지정하거나,
함수를 지정 가능 -> 매개변수로 호출되기 직전 상태값을 받는다. -> 선호
setter에 지정된 함수에서 상탯값을 직접 참조하고 있지 않아도, "직전 상탯값"을 인자로 전달받기에 유용.
immer 라이브러리와 엮어 쓰기에도 좋습니다.



### setState를 통하지 않고 state 값을 직접 변경하면, UI에 자동 반영 X
UI에 강제반영하기 위해 this.forceUpdate(); 를 사용
클래스형 컴포넌트 생성자에서는 setState 호출은 ...
무시됩니다.
setState 호출은 컴포넌트가 마운트된 이후에만 유효하기 때문
데이터를 가져오기 위해 API를 호출하고 그 응답을 state에 반영코자 할 경우에
- componentDidMount 메서드를 활용
- 함수형 컴포넌트에서는 useEffect(() => {}, []) 훅을 활용



### 상탯값을 어디에 저장/관리할 것인가?
1) 컴포넌트 내부
각 컴포넌트 객체 단위로 상탯값을 유지하고, 하위 컴포넌트의 속성값으로 전달
상탯값 setter 함수를 통해 상탯값을 직접 변경 (물론 Reducer 개념을 적용할 수도)
this.setState 함수, useState 훅을 활용
문제점 : 컴포넌트 계층이 복잡할 때, 상탯값/속성값 전파의 번거로움.
하지만, 리액트 16.3에 소개된 Context API로 전파가 쉬워졌습니다.
2) 컴포넌트 외부에서 "전역 상태 관리"
컴포넌트 외부에 별도의 상탯값 저장소를 둡니다.
여러 컴포넌트들에 의해 공유될 상탯값 (로그인 정보 등)들을 관리합니다.
모든 상탯값들을
컴포넌트에게 상탯값 setter 함수를 제공하기보다, dispatch 함수를 제공합니다.



## 속성값

### 속성값
컴포넌트 생성 시에 넘겨지는 값의 목록
	읽기 전용으로 취급하고, 변경하지 않습니다.
	자식 컴포넌트 입장에서는 데이터/함수를 전달받는 유일한 통로 (But, Context API로 인해, 새로운 통로가 생겼	어요.)
	부모 컴포넌트의 데이터/함수를 자식 컴포넌트에게 넘겨주게 됩니다.
	컴포넌트는 HOC (High Order Components) 기법을 통해, Redux의 값이나 함수를 넘겨 받기도 합니다.
값 지정 시에 중괄호를 통해 다양한 타입의 값 및 표현식 지정 가능.
	중괄호를 빼면, 문자열 타입의 값만 지정 가능



## 속성값 타입 및 디폴트값 정의하기

### 각 속성값에 대한 타입 명시 및 필수 여부 지정하기 -> 생산성
TypeScript와 같은 정적 언어를 사용하거나,
prop-types 팩키지를 통해 속성값에 타입을 지정할 수 있습니다.
설치> yarn add prop-types
지원 타입
https://github.com/facebook/prop-types#usage