/*
alert('hello ');
alert('你好')
*/
name='zhangsan'; //全局变量
var age = '24'; //局部变量
//函数
function Foo(){
    var arg1 = arguments[0];
    console.log(name);
    console.log(arg1);
}
Foo('GG');

//匿名函数
var func = function(){
    console.log('我是匿名函数')
}
func();

//自执行函数，不用调用，自动执行
(function(){
    console.log('我是自执行函数');
})();

(function(name){
    console.log('我是自执行函数--带参数'+name);
})('zhangsan');

//字符串常用方法
/*
trime()
charAt(index)
substring(start,end)
.....
*/

//for循环，数组
var arr = [1,2,3,4]
//var arr1 = Array()[1,2,3,4]
arr.push(5) //追加
arr.unshift(0)//最前面插入
arr.splice(1,0,'boy')
console.log(arr)
//删除 arr.pop()
//arr.shit()
//截取 arr.slice(start,end)
//合并 arr.concat(arr2)
//翻转 arr.converse()
//字符串格式化 arr.join('-)
//长度 arr.length

for(var i=0;i<=5;i++){
    console.log(i)
}
var a = [11,22,33,44,55,66]
for(var i in a){
    console.log(a[i])
}




