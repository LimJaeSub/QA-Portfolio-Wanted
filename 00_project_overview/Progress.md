# 🚀 QA Portfolio 진행상황

**프로젝트명**: Wanted.co.kr QA 테스트 종합 프로젝트  
**목표**: 실무 수준의 QA 포트폴리오 완성

---

## 📅 Week 1: 기반 작업 + 수동 테스트

### ✅ Day 1 - 완료


**작업 내용**
- [x] GitHub 레포지토리 생성
- [x] 프로젝트 폴더 구조 생성
- [x] test-plan.md 작성 완료 (추후 수정 필요시 수정)
- [x] 원티드 사이트 탐색 및 기능 분석
- [x] 테스트 범위 정의


**산출물**: 
- `00-project-overview/test-overview.md`
- 기본 폴더 구조


**배운점**:
- 자동화 판단 기준: 핵심 기능,Form 입력/검증,데이터 기반,CRUD,단순 반복 작업
- UI/UX , 일회성이나 자주 바뀌는 것,탐색적 테스트는 수동 테스트
---

### ✅ Day 2 - 진행중


**작업 내용**
- [x] test-plan.md 작성 완료
- [x] Menu Tree 시트 설계
- [x] test-cases.xlsx 구조 설계


**산출물**:
- `01-manual-testing/test-plan.md`
- `test-cases.xlsx` (Google Sheets - 작업 중)
- `PROGRESS.md`

**배운점**:
- Menu Tree는 테스트 커버리지, TC를 작성하여 Menu Tree에 적용시키면서 테스트 커버리지를 측정
- 테스트 프로세스 개념 재확립
- 실무에서는 Excel → Jira 순서로 작업
---

### 📝 Day 3 - 예정

**계획**
- [ ] Menu Tree 최종 완성
- [ ] 테스트 케이스 작성 완료
- [ ] 수동 테스트 실행 시작 (검색 기능)
- [ ] 테스트 실행 로그 작성 시작
- [ ] 버그 발견 시 임시 기록
- [ ] 스크린샷 캡처

**목표 산출물**:
- 완성된 Menu Tree
- TC-001 ~ TC-010 실행 결과
- screenshots/ 폴더

---

### 📝 Day 4 - 예정

**계획**
- [ ] 수동 테스트 계속 (필터/정렬/공고상세)
- [ ] TC-011 ~ TC-020 실행
- [ ] 버그 리포트 작성 시작
- [ ] 스크린샷 정리

---

### 📝 Day 5 - 예정

**계획**
- [ ] 수동 테스트 완료 (UI/UX, 반응형)
- [ ] TC-021 ~ TC-030 실행
- [ ] test-execution-log.md 작성
- [ ] 발견된 버그 정리 및 우선순위 분류
- [ ] test-cases.xlsx 최종본 다운로드 및 푸시

**마일스톤**: Week 1 완료 ✨

---

## 📅 Week 2: 자동화 + API 테스트

### 📝 Day 6 - 예정

**계획**
- [ ] Selenium 환경 구축
- [ ] requirements.txt 작성
- [ ] base_page.py 작성 (Page Object Model)
- [ ] config.py 설정
- [ ] 첫 자동화 스크립트 (메인 페이지 로딩)

---

### 📝 Day 7 - 예정

**계획**
- [ ] 검색 기능 자동화
  - search_page.py 작성
  - test_search.py 작성 (5개 케이스)
- [ ] 테스트 실행 및 디버깅

---

### 📝 Day 8 - 예정

**계획**
- [ ] 필터 기능 자동화
  - test_filter.py 작성 (4개 케이스)
- [ ] 공고 상세 자동화
  - job_detail_page.py 작성
  - test_job_detail.py 작성

---

### 📝 Day 9 - 예정

**계획**
- [ ] 네비게이션 자동화 (test_navigation.py)
- [ ] 나머지 자동화 스크립트 완성
- [ ] 코드 리팩토링
- [ ] 테스트 리포트 생성 설정

---

### 📝 Day 10 - 예정

**계획**
- [ ] Chrome DevTools로 API 분석
- [ ] Postman 컬렉션 생성
  - 검색 API
  - 공고 목록 API
  - 공고 상세 API
- [ ] API 테스트 실행 및 결과 문서화
- [ ] 자동화 README.md 작성

**마일스톤**: Week 2 완료 ✨

---

## 📅 Week 3: 성능 + Jira + 최종 정리

### 📝 Day 11 - 예정

**계획**
- [ ] Lighthouse 성능 분석 (주요 페이지 5개)
- [ ] Chrome DevTools Network 분석
- [ ] 성능 개선 제안서 작성
- [ ] lighthouse-reports/ 생성

---

### 📝 Day 12 - 예정

**계획**
- [ ] Jira 프로젝트 생성 및 설정
- [ ] 커스텀 필드 설정
- [ ] 워크플로우 구성
- [ ] Epic 생성 (3-4개)
- [ ] 버그 이슈 등록 시작

---

### 📝 Day 13 - 예정

**계획**
- [ ] 버그 이슈 등록 완료
- [ ] 대시보드 구성
- [ ] 차트 생성
- [ ] Jira 스크린샷 캡처
- [ ] bug-analysis.md 작성

---

### 📝 Day 14 - 예정

**계획**
- [ ] executive-summary.md 작성
- [ ] test-metrics.md 작성
- [ ] improvement-suggestions.md 작성
- [ ] 최종 보고서 검토

---

### 📝 Day 15 - 예정

**계획**
- [ ] README.md 완성
- [ ] 모든 문서 링크 확인
- [ ] 스크린샷 정리
- [ ] 코드 최종 리뷰
- [ ] Git 커밋 히스토리 정리
- [ ] 최종 푸시

**마일스톤**: 프로젝트 완료! 🎉

---

## 📈 주요 지표


### 산출물 현황
```
문서:
✅ test-overview.md
✅ test-plan.md
⏳ test-cases.xlsx (작업 중)
⬜ test-execution-log.md
⬜ bug-reports/ (0건)
⬜ automation scripts (0/15)
⬜ 최종 보고서

코드:
⬜ Page Objects (0/5)
⬜ Test Scripts (0/4)
⬜ Config files
```

### 테스트 진행률
- **수동 테스트**: 0/30 (0%)
- **자동화 테스트**: 0/15 (0%)
- **API 테스트**: 0/8 (0%)
- **버그 발견**: 0건

---

## 🎯 현재 주차 목표

**Week 1 (진행 중)**
- [x] 프로젝트 세팅
- [x] 테스트 계획 수립
- [ ] 30개 테스트 케이스 100% 실행
- [ ] 5개 이상 버그 발견
- [ ] test-cases.xlsx 완성

---


## 🐛 발견된 이슈 (임시 메모)

### 우선순위 분류 전
```
(버그 발견 시 여기에 간단히 메모)

예시:
- [날짜] 필터 초기화 안 됨
- [날짜] 모바일 레이아웃 깨짐
```

---


## 🔗 참고 자료
- [Selenium 공식 문서](https://www.selenium.dev/documentation/)
- [Wanted 사이트](https://www.wanted.co.kr/)

---
