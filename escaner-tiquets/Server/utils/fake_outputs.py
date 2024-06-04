fake_products = {
    'nom': "MERCADONA, S.A. A-12345678",
    'adressa': 'C/ JOSEP MARÍA FOLCH I TORRES, 5',
    'ciutat': "TARRAGONA 43006",
    'telf': "977598991",
    'data': "22-04-2024",
    'op': "12345",
    'factura_simplificada': "1234-123-12345",
    'barcode': 'image',                   
    'total_amb_IVA': '303,93',
    'pagat_targeta_bancaria': '303,93',
    'total_sense_IVA': '202,33',
    'iva_total': '50,33',
    'targeta_bancaria': "**** **** **** **** 1234",
    'NC': '123456789',
    'AUT': '123456',
    'AID': "B0000000012345",
    'ARC': '1234',
    'targeta_1': 'VISA CREDITO/DEB',
    'targeta_2': 'Visa CaixaBank',
    'logo_bottom': 'image',
    'logo_top': 'image',
    'logo_contact_less': 'image',
    'products': [
        {
            'descripcio': 'BAIETA PAL SUAU',
            'quantitat': '3',
            'preu_unitari': '0,85',
            'import': '2,54'
        },
        {                      
            'descripcio': 'SECRET DE PORC',
            'quantitat': '1',
            'preu_unitari': '2,60',
            'import': '2,60'
        },
        {
            'descripcio': 'AIGUA MINERAL',
            'quantitat': '2',
            'preu_unitari': '0,22',
            'import': '0,44'
        },
        # {
        #     'descripcio': 'SORRA PER GAT',
        #     'quantitat': '3',
        #     'preu_unitari': '3,63',
        #     'import': '10,89'
        # },
        # {
        #     'descripcio': 'FORMATGE RATLLAT',
        #     'quantitat': '1',
        #     'preu_unitari': '1,25',
        #     'import': '1,25'
        # },
        # {
        #     'descripcio': 'FORMATGE FRESC',
        #     'quantitat': '1',
        #     'preu_unitari': '1,55',
        #     'import': '1,55'
        # },
        # {
        #     'descripcio': 'NATILLES',
        #     'quantitat': '1',
        #     'preu_unitari': '3,06',
        #     'import': '3,06'
        # },
        # {
        #     'descripcio': "OLI D'OLIVA SUAU",
        #     'quantitat': '1',
        #     'preu_unitari': '14,25',
        #     'import': '14,25'
        # },
        # {
        #     'descripcio': 'BEGUDA LÀCTIA',
        #     'quantitat': '1',
        #     'preu_unitari': '1,91',
        #     'import': '1,91'
        # },
        # {
        #     'descripcio': 'DISCOS',
        #     'quantitat': '1',
        #     'preu_unitari': '172,42',
        #     'import': '172,42'
        # },
        # {
        #     'descripcio': 'ALVOCAT',
        #     'quantitat': '5',
        #     'preu_unitari': '1,86',
        #     'import': '9,31'
        # },
        # {
        #     'descripcio': 'RECANVIS MAQUINETA',
        #     'quantitat': '1',
        #     'preu_unitari': '67,71',
        #     'import': '67,71'
        # },
        # {
        #     'descripcio': 'ENTRECOT BOVÍ',
        #     'quantitat': '1',
        #     'preu_unitari': '11,15',
        #     'import': '11,15'
        # },
        # {
        #     'descripcio': 'POLLASTRE SALTAT',
        #     'quantitat': '0.707',
        #     'preu_unitari': '4,40',
        #     'import': '3,11'
        # },
        # {
        #     'descripcio': 'GARRÓ DE PORC',
        #     'quantitat': '1',
        #     'preu_unitari': '1,74',
        #     'import': '1,74'
        # }
    ],
    'ivas': [
        {
            'valor': '21%', 
            'base_imposable': 
            '44,01', 'quota': 
            '9,24',
        },
        {
            'valor': '10%', 
            'base_imposable': '3,48', 
            'quota': '0,35'
        },
        {
            'valor': '4%', 
            'base_imposable': '0,47', 
            'quota': '0,02'
        }
    ]
}

fake_image = "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"

fake_audio = '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vfdb6dubOvP+r2F/0wmjUcRjjbFzXmjq1mCNpAIw2uKACBhgQGZQtAgyEE0ZGTsKILqKNsUE852jguG211nE6jKxIvGa5OkYRo0Y9eFAW////z+f//NExAgUGxrAABBQvTx69S/3sr/////55/1nv/r/+P4+OKq4bveYW4nkXUW3kKgBhBPCNS1anHPBcQQhrjx4wcJcVgXKIhhQ1S6D10Yo4Og9YORYfMr3/////po6///2//NExAoRcxbAAAhKub2v///9NX5u3T/azs7U1ZS0sVSniA9xABQ67CJSmdSCItGh0cU0RMHSHVBrKORmEUKZwFGB1xCKhYSMVvL/////8viF//8p+f+///2o7//X9UdK//NExBcRGx6sAAhKvO3VuXdDCIiKuh2EQ6EhaOFnKqmRxYRFTILLYcQPCUqIH2EhzuKiIgAwsHWDolUVLEQVv//8/+a+U//7+YS1bU1u5321b+p3/6d/XzqOvvznR86c//NExCUR2wqMAChOufQ7Q8jWcykTY6D0ajUbOaaQEYJipqHID4kOg9Isaw6NTVeqARokgXcnAqmZaNdTt/9fX//ZP2vf5fq2n/obVi/mq3M//9HX5nMa5cukzulN5lKy//NExDARMt5cAU0QAZXVipeZWkMGOysKVFUZwYlqVUlUXjcp8y8Kv0pnCoM8sLtex+9Xrd1+6qv+lcTZLNPWncYnV2fpYhr1uDVHi7Dy6pYiOtWiWUssRyhEC1LEetcU//NExD4g4ypMAZhAAPY53x5BhwtZoscHUevtE3y8D3t7lxtjBllUJxFGg3HiEIAcEmyqw320kk/VK8IkoQIgNw/vwqIYUBuDIVA8VCIFw88OgmrOvGnchJl3b+OSkO3F//NExA0UUQ6cAZhYAHVh2oykO65vekfsHapZfn1jexYSyDHYUsq2UVsSk6SzqO/+viYRWPcQne4OuKXK7KAAfyj7e7q2EIt9D0biooDMedFaaq9WIssF+sSYM3IHYARV//NExA4U8SakAdh4ADVxXOJgrDQMXnQWi0qZBFaaegCTXNYbIuG5eVrEr1OPIfquHITEuWst0Xf3XH+86vf+80fKsTjXZ44bWlxP7dBo3////6ps+wQhNI2wXBT1nkHT//NExA0SASKwAHvecBbE8BAp25Mwgz65PxW02pGGDeIc6pb344CxQjkBSDyYniEONcv4vz67//zeucYfXhajZmsR/+/////ojGOCRyUNuUDrolSV0M5D8fVrkG4ARgma//NExBgSoRaoAMYecEdAOY92FRe1+netiUijEZCPOnANYBxPFrURoxZHr62M/X1v418wK2vDhPpBYKlTFP6ZOoJqUIVqzXK4SjhFRebwR9CdstWwpkDGnAWx07SBo56l//NExCARcRKkAMPwcUKzR+G2jT/CEqashgBdsZsyuXWvqZa3r/w3/MLuO7Hcq04u1duucq/bDus2jFKAjTvCoFbv4sDPOuAaqpdqgS0JSkVuA3o5m5sVNN0GRI5SZPRv//NExC0SYRacAMPwcGn7E6XDDuGH48/956r3vz3Y5ajNnoJBltvZ596KpflAVJjyOJY8zVnx9DyhQqGruMO5zVx+sDt9FtCisMVfHIaKynTnTT/s27yanzNn+1fem7yP//NExDYRERaoAMPecFthaxLDATyIqpLK02Pj6n3lXRBHUyUWHma3AYBI8Lt3F2GMyOy6g0WxVMrC8eR49kV3zYS5OoFTDGcW1FO6P4vxFp5a/dvj399alj91WsPYqMcn//NExEQRaSaUAMvecH9VbPD0CCPqdoU/CI2mgJNOi2uVXh4SWeUkaz9Rp3zFbOXt4auV214H9H0/r4E1Lwt5vr41/i3+v5a1iHzbnyX/ez///+/1KncaijIZ1cVpXKab//NExFERSRaMAMvecGJKNBUcGiZ5w0UmOPXl0mcrL+KrS4AIuTND6j4c3////55h0UkAK/y+8Tl3fv/pIfRdYTs/8j4YKZ4SIBqIUuFVFFzZbv/+/5zPlL///8yl///9//NExF4QwRaQAMpWcJELONv/oV9W0rSRTrT0IShGIBvUDAzZRZ7tkPf9J3yMclVyMHIEEZj6wx1/////5f//////////8fxP//8///Xys83099dzNdaK1FFigQB/Yoo2//NExG4Q4wKgAIBEudHotykaS2W6uTy7gcfZPNyhDrM9mh4OGi4kpFVMb/////l56///f7f///9O/b/9kdS2oahWTWqGaLipwsDCIsDiZDXQ4WLnHh1Acwk44CCalUzO//NExH0RSxq0ABBQvDziZh6DA4LjFApxMWDgUDF1D/////+v/////////6t//tzM1pXZNLneqHZxGxBERFw4cVD4uMIBhUTEo/FRUSFSAKJDhcBx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'

__all__ = ['fake_image', 'fake_products', 'fake_audio']