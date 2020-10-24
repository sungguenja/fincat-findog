const data = [
  {
    id: 1,
    name: '고양이1',
    image: 'https://ifh.cc/g/maXKFd.jpg'
  },
  {
    id: 2,
    name: '고양이2',
    image: 'https://ifh.cc/g/JDG31b.jpg'
  }
]

export default {
  list(query) {
    return new Promise(res => {
      setTimeout(()=> {
        res(data)
      }, 200);
    })
  }
}