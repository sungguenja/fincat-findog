import FormView from '../views/FormView.js'
import ResultView from '../views/ResultView.js'

import KeywordView from '../views/KeywordView.js'


import SearchModel from '../models/SearchModel.js'
import KeywordModel from '../models/KeywordModel.js'


const tag = '[MainController]'

export default {
  init() {
    FormView.setup(document.querySelector('form'))
      .on('@submit', e => this.onSubmit(e.detail.input))
      .on('@reset', e => this.onResetForm())
    

    
    KeywordView.setup(document.querySelector('#search-keyword'))
      .on('@click', e => this.onClickKeyword(e.detail.keyword))
    


    ResultView.setup(document.querySelector('#search-result'))

    this.renderView()
  },
  search(query) {
    FormView.setValue(query)
    SearchModel.list(query).then(data => {
      this.onSearchResult(data)
    })
  },
  renderView() {
    console.log(tag, 'rednerView()')

    ResultView.hide()
  },
  fetchSearchKeyword() {
    KeywordModel.list().then(data => {
      KeywordView.render(data)
    })
  },
  fetchSearchHistory() {
    HistoryModel.list().then(data => {
      const a = HistoryView.render(data)
        a.bindRemoveBtn()
    })
  },

  onSubmit(input) {
    console.log(tag, 'onSubmit()', input)
    this.search(input)
  },
  onResetForm() {
    console.log(tag, 'onResetForm()')
    this.renderView()
  },
  onSearchResult(data) {
    TabView.hide()
    KeywordView.hide()
    HistoryView.hide()
    ResultView.render(data)
  },
  onChangeTab(tabName) {
    this.selectedTab = tabName
    this.renderView()
  },
  onClickKeyword(keyword) {
    this.search(keyword)
  },
  onClickHistory(keyword) {
    this.search(keyword)
  },
  onRemoveHistory(keyword) {
    HistoryModel.remove(keyword)
    this.renderView()
  }
}