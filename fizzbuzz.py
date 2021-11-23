fruits = ['Apple', 'Banana', 'Pineapple', 3]

animals = [
        'Lion',
        'Tiger',
        'Rabbit',
        3
        ]

clubs = [
    'ManU',
    'ManC',
    3,
]

for (let i=1; i <= 16 ; i++){
        if(i%15 === 0){
            console.log('fizzbuzz')
        }
        else if(i%3 === 0){
            console.log('fizz')
        } else if(i%5 === 0){
            console.log('buzz')
        } else{
            console.log(i)
        }
}
