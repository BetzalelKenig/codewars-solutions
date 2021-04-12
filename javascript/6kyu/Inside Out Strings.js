// You are given a string of words (x), for each word within the string you need to turn the word 'inside out'. By this I mean the internal letters will move out, and the external letters move toward the centre.

// If the word is even length, all letters will move. If the length is odd, you are expected to leave the 'middle' letter of the word where it is.

// An example should clarify:

// 'taxi' would become 'atix' 'taxis' would become 'atxsi'

const insideOut = x => x.split(' ').map(w => w.length < 3 ? w : [...w.split('').slice(0, Math.floor(w.length / 2)).reverse(), w.length % 2 == 0 ? '' : w[Math.floor(w.length / 2)], ...w.split('').slice(Math.ceil(w.length / 2), w.length).reverse()].join('')).join(' ')
