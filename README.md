# QA-Portfolio-Wanted

> **실제 서비스(원티드) 대상 E2E QA 자동화 프로젝트**
> Selenium + pytest + POM 패턴으로 구성한 UI 자동화 포트폴리오

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **테스트 대상** | [wanted.co.kr](https://www.wanted.co.kr) (실제 서비스) |
| **테스트 유형** | UI E2E 자동화 |
| **프레임워크** | Python + Selenium 4 + pytest |
| **아키텍처** | Page Object Model (POM) |
| **CI/CD** | GitHub Actions |
| **총 TC 수** | 13개 (Search 3, Header 3, Main 3, Job List 2, Job Detail 2) |

---

## 🗂 프로젝트 구조

```
QA-Portfolio-Wanted/
├── 01_automation_testing/
│   ├── config/
│   │   └── config.py              # URL, 타임아웃 등 설정값 분리
│   ├── pages/                     # Page Object Model
│   │   ├── base_page.py           # 공통 메서드 15개+ (find, click, wait 등)
│   │   ├── header_component.py    # 헤더 컴포넌트 (재사용 가능한 설계)
│   │   ├── search_page.py
│   │   ├── main_page.py
│   │   ├── job_list_page.py
│   │   └── job_detail_page.py
│   ├── tests/                     # 테스트 모듈
│   │   ├── test_search_flow.py
│   │   ├── test_search_modal.py
│   │   ├── test_header.py
│   │   ├── test_main_page.py
│   │   ├── test_job_list.py
│   │   └── test_job_detail.py
│   ├── conftest.py                # 드라이버 설정 + 실패 시 스크린샷 자동 캡처
│   └── requirements.txt
└── .github/
    └── workflows/
        └── test.yaml              # GitHub Actions CI
```

---

## 🧪 테스트 전략

### 테스트 범위

```
원티드 주요 사용자 플로우
├── 검색 기능     검색 모달 → 키워드 입력 → 결과 확인 → 예외 처리
├── 헤더 내비게이션  로고 클릭 → 메인 복귀 / 메뉴 이동 / 반응형 BVA
├── 메인 페이지    페이지 로드 / Shortcut 메뉴 / 슬라이더
├── 채용 목록     직군 필터 / 지역 필터 (계층적 3단계)
└── 채용 상세     상세 진입 / 포지션 섹션 구조 검증
```

### 설계 원칙

- **POM 패턴**: 페이지별 로케이터와 액션을 캡슐화해 유지보수성 확보
- **컴포넌트 분리**: `header_component.py`를 독립 객체로 분리해 여러 테스트에서 재사용
- **Explicit Wait**: `WebDriverWait` + `expected_conditions` 활용
- **실패 스크린샷**: `conftest.py`에서 테스트 실패 시 자동 캡처
- **Skip 사유 명시**: `@pytest.mark.skip(reason=...)` 으로 스킵 사유 코드에 기록

---

## 📋 테스트 케이스 목록

### Search (검색)

| TC ID | 테스트 명 | 핵심 포인트 | 결과 |
|-------|----------|------------|------|
| TC_001 | 검색 전체 플로우 | E2E: 모달 오픈 → 키워드 입력 → 결과 페이지 → URL 검증 | ✅ PASS |
| TC_003 | 공백 검색어 입력 검증 | Edge Case: Toast UI 에러 메시지 확인 | ✅ PASS |
| TC_005 | 자동완성 기능 | 동적 UX: 키워드 매칭 로직 검증 | ✅ PASS |

### Header (헤더)

| TC ID | 테스트 명 | 핵심 포인트 | 결과 |
|-------|----------|------------|------|
| TC_025 | 로고 클릭 → 메인 이동 | Navigation: 다른 페이지에서 로고 클릭 → 메인 URL 검증 | ✅ PASS |
| TC_026 | 메뉴 클릭 → 페이지 이동 (5개) | Parametrized: jobs/event/resume/content/community 일괄 검증 | ✅ PASS |
| TC_037 | 반응형 햄버거 메뉴 (992px) | **BVA**: 991px(보임) / 992px(숨김) 경계값 + Locator 정밀도 | ✅ PASS |

### Main Page (메인)

| TC ID | 테스트 명 | 핵심 포인트 | 결과 |
|-------|----------|------------|------|
| TC_027 | 페이지 로드 확인 | 교차 검증: 타이틀 + URL 동시 확인 | ✅ PASS |
| TC_029 | Shortcut 메뉴 클릭 | 동적 Locator: `data-kind` 속성 활용 → URL 변경 확인 | ✅ PASS |
| TC_035 | 슬라이더 네비게이션 | 동적 UI: viewport 기반 카드 추출 → 좌우 이동 → 복귀 검증 | ✅ PASS |

### Job List (채용 목록)

| TC ID | 테스트 명 | 핵심 포인트 | 결과 |
|-------|----------|------------|------|
| TC_015 | 직군 필터 (개발 > QA) | 계층적 필터: 대분류 → 소분류 스크롤 → 키워드 매칭 | ✅ PASS |
| TC_017 | 지역 필터 (한국 > 서울 > 관악구) | **3단계 계층**: 드롭다운 → 스크롤 선택 → URL 파라미터 검증 | ✅ PASS |

### Job Detail (채용 상세)

| TC ID | 테스트 명 | 핵심 포인트 | 결과 |
|-------|----------|------------|------|
| TC_019 | 상세 페이지 로드 확인 | E2E: `position_id` 추출 → 클릭 → URL에 ID 포함 검증 | ✅ PASS |
| TC_021 | 포지션 상세 섹션 확인 | 스크롤+구조: `scroll_and_find` → h2 + h3 + span 복합 검증 | ✅ PASS |

---

## 🐛 발견 결함

> ⚠️ 실제 서비스 대상 탐색적 테스트 중 발견한 이슈는 아래와 같습니다.
> (자동화 테스트 설계 과정에서 확인된 동작 이슈)

| ID | 제목 | 심각도 | 상태 |
|----|------|--------|------|
| BUG-001 | 햄버거 메뉴 CSS 브레이크포인트 오프셋 (16px 차이) | Minor | 자동화 TC에 BVA로 커버 |

---

## ⚙️ 실행 방법

### 사전 요구사항

- Python 3.9+
- Chrome 브라우저 + ChromeDriver (버전 일치 필요)

### 설치

```bash
git clone https://github.com/LimJaeSub/QA-Portfolio-Wanted.git
cd QA-Portfolio-Wanted/01_automation_testing
pip install -r requirements.txt
```

### 테스트 실행

```bash
# 전체 실행
pytest tests/ -v

# 특정 모듈만 실행
pytest tests/test_search_flow.py -v

# 특정 TC만 실행
pytest tests/ -k "TC_037" -v

# Headless 모드
pytest tests/ --headless -v
```

### CI/CD

`main` 브랜치 push 또는 PR 시 GitHub Actions가 자동으로 테스트를 실행합니다.

---

## 🛠 기술 스택

| 구분 | 기술 |
|------|------|
| 언어 | Python 3.9+ |
| 자동화 | Selenium 4 |
| 테스트 프레임워크 | pytest |
| 아키텍처 | Page Object Model |
| CI/CD | GitHub Actions |
| 브라우저 | Chrome (Headless 지원) |

---

## 💡 주요 기술 포인트

**1. BasePage — 15개+ 공통 메서드**
페이지 공통 동작(find, click, wait, scroll 등)을 BasePage로 추상화해 각 페이지 객체의 코드 중복을 최소화했습니다.

**2. 컴포넌트 단위 POM**
`header_component.py`를 독립 컴포넌트로 분리해 여러 페이지 테스트에서 재사용 가능한 구조로 설계했습니다.

**3. 반응형 BVA (TC_037)**
CSS 브레이크포인트 992px를 경계값 분석으로 검증. 991px(햄버거 보임) / 992px(햄버거 숨김) 두 케이스를 모두 자동화했습니다.

**4. 동적 스크롤 처리 (TC_017, TC_021)**
긴 드롭다운과 긴 페이지에서 요소를 찾기 위한 반복 스크롤 로직(`scroll_and_find`)을 구현했습니다.

---

## 📬 Contact

[![Email](https://img.shields.io/badge/Email-liso__o@naver.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:liso_o@naver.com)
